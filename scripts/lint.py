#!/usr/bin/env python3
# DEPENDENCIES:
#     $ pip3 install 'PyYAML>=5,<6'
# FORMAT:
#     $ isort scripts/lint.py
#     $ yapf --style='{ COLUMN_LIMIT: 9999 }' --in-place scripts/lint.py
#     $ mypy scripts/lint.py
import argparse
import pathlib
import re
import sys
from logging import DEBUG, basicConfig, getLogger
from typing import *

import yaml

logger = getLogger(__name__)


class Message(NamedTuple):
    type: str
    file: pathlib.Path
    line: int
    col: int
    message: str

    def __str__(self) -> str:
        return '::{} file={},line={},col={}::{}'.format(self.type, str(self.file), self.line, self.col, self.message)


def warning(message: str, *, file: pathlib.Path, line: int, col: int) -> Message:
    assert line >= 1 or line == -1
    assert col >= 1 or line == -1
    return Message(type='warning', file=file, line=line, col=col, message=message)


def error(message: str, *, file: pathlib.Path, line: int, col: int) -> Message:
    assert line >= 1 or line == -1
    assert col >= 1 or line == -1
    return Message(type='error', file=file, line=line, col=col, message=message)


def collect_messages_from_line(msg: str, *, path: pathlib.Path, line: int) -> List[Message]:
    result: List[Message] = []

    def warning_by_regex(pattern: str, text: str) -> None:
        nonlocal result
        m = re.search(pattern, msg)
        if m:
            result.append(warning(text, file=path, line=line, col=m.start() + 1))

    def error_by_regex(pattern: str, text: str) -> None:
        nonlocal result
        m = re.search(pattern, msg)
        if m:
            result.append(error(text, file=path, line=line, col=m.start() + 1))

    error_by_regex(
        pattern=r'です。|ます。',
        text='日本語: 敬体ではなく常体を使ってください。',
    )
    error_by_regex(
        pattern=r'，|．',
        text="日本語: `，` と `．` ではなく `、` と `。` を使ってください。",
    )

    error_by_regex(
        pattern=r'\\\\',
        text=r"KaTeX: `\\` ではなく `\cr` を使ってください。`\\` が Markdown でのエスケープと解釈されて壊れることがあります。",
    )
    error_by_regex(
        pattern=r'\\{|\\}',
        text=r"KaTeX: `\{` と `\}` ではなく `\lbrace` と `\rbrace` を使ってください。`\{` や `\}` が Markdown でのエスケープと解釈されて壊れることがあります。",
    )
    error_by_regex(
        pattern=r'_{',
        text=r"KaTeX: `a_{i + 1}` ではなく `a _ {i + 1}` を使ってください。`_` のまわりに空白がないと、Markdown の強調と解釈されて壊れえることがあります。",
    )

    warning_by_regex(
        pattern=r'捜査',
        text=r"typo: `捜査` ではなく `走査` の可能性があります。",
    )

    error_by_regex(
        pattern=r'\$\w *\\to *\w\$ *最短経路',
        text=r"typo: `$s \to t$ 最短経路` ではなく `$s$-$t$ 最短経路` と書いてください。(https://github.com/kmyk/algorithm-encyclopedia/pull/43)",
    )
    error_by_regex(
        pattern=r'辺 *\$\w *\\to *\w\$',
        text=r"typo: `有向辺 $x \to y$` ではなく `有向辺 $(x, y)$` と書いてください。(https://github.com/kmyk/algorithm-encyclopedia/pull/44)",
    )
    error_by_regex(
        pattern=r'辺 *\$\w *\$? *- *\$? *\w\$',
        text=r"typo: `無向辺 $x - y$` ではなく `無向辺 $\lbrace x, y \rbrace$` と書いてください。(https://github.com/kmyk/algorithm-encyclopedia/pull/44)",
    )

    return result


def collect_messages_from_yaml_frontmatter(frontmatter: Dict[str, Any], *, path: pathlib.Path) -> Iterator[Message]:
    required_keys = [
        'layout',
        'authors',
        'reviewers',
        'date',
        'updated_at',
        'tags',
        'description',
    ]
    for key in required_keys:
        if key not in frontmatter:
            yield error('YAML frontmatter: `{}` が存在しません。'.format(key), file=path, line=-1, col=-1)
            return
    yield from collect_messages_from_line(frontmatter['description'] or '', path=path, line=-1)

    if not frontmatter.get('draft') and not frontmatter.get('authors'):
        yield error('YAML frontmatter: `authors` を設定してください。', file=path, line=-1, col=-1)


def collect_messages_from_file(path: pathlib.Path) -> Iterator[Message]:
    with open(path) as fh:
        lines = list(fh.readlines())

    if not lines:
        yield error('file: ファイルが空です。YAML frontmatter がありません。', file=path, line=-1, col=-1)
        return
    if lines[0].rstrip() != '---':
        yield error('file: YAML frontmatter がありません。ファイルの1行目は `---` であるべきです。', file=path, line=-1, col=-1)
        return
    for i in range(1, len(lines)):
        if lines[i].rstrip() == '---':
            frontmatter_str = ''.join(lines[1:i])
            try:
                frontmatter = yaml.load(frontmatter_str)
            except yaml.YAMLError as e:
                yield error('file: YAML frontmatter のパースに失敗しました: {}'.format(e), file=path, line=-1, col=-1)
                return
            offset = i + 1
            body = lines[offset:]
            break
    else:
        yield error('file: YAML frontmatter がありません。ファイルの2行目以降に `---` が見つかりませんでした。', file=path, line=-1, col=-1)

    yield from collect_messages_from_yaml_frontmatter(frontmatter, path=path)
    for i, line in enumerate(body):
        yield from collect_messages_from_line(line, path=path, line=offset + i + 1)


def list_markdown_files() -> List[pathlib.Path]:
    basedir = pathlib.Path.cwd()
    paths: List[pathlib.Path] = []
    paths.extend(basedir.glob('_algorithms/**/*.md'))
    paths.extend(basedir.glob('_tenkeis/**/*.md'))
    paths = [path.resolve().relative_to(basedir) for path in paths]
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    basicConfig(level=DEBUG)

    paths = list_markdown_files()
    warning_count = 0
    error_count = 0
    for path in paths:
        logger.info('checking %s', str(path))
        for message in collect_messages_from_file(path):
            if message.type == 'error':
                error_count += 1
            elif message.type == 'warning':
                warning_count += 1
            else:
                assert False
            print(message)
    logger.info('%d errors and %d warnings in %d files', error_count, warning_count, len(paths))
    if error_count:
        logger.error('WA')
        return 1
    logger.info('AC')
    return 0


if __name__ == '__main__':
    sys.exit(main())
