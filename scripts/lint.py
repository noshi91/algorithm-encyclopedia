#!/usr/bin/env python3
import argparse
import datetime
import functools
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


@functools.lru_cache(maxsize=None)
def list_defined_users() -> FrozenSet[str]:
    path = pathlib.Path('_sass', 'user-colors.scss')
    with open(path) as fh:
        lines = fh.readlines()

    users: List[str] = []
    for line in lines:
        for user in re.findall(r'.user-(\w+)', line):
            users.append(user)
    return frozenset(users)


def collect_messages_from_line(msg: str, *, path: pathlib.Path, line: int) -> List[Message]:
    # Ignore errors and warnings in quoted texts
    if msg.lstrip().startswith('>') or 'blockquote' in msg:
        return []

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
        pattern=r'^\$$',
        text=r"KaTeX: display 表示をしたいときは `$` ではなく `$$` を使ってください。`$` は inline 表示になります。",
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
        text=r"KaTeX: `a_{i + 1}` ではなく `a _ {i + 1}` を使ってください。`_` のまわりに空白がないと、Markdown の強調と解釈されて壊れることがあります。",
    )
    error_by_regex(
        pattern=r'\$.*\|.*\$',
        text=r"KaTeX: 絶対値記号などには `|` や `\|` ではなく `\vert` や `\lvert` `\rvert` を使ってください。`|` は Markdown のテーブルと解釈されて壊れることがあり、また `\|` は Markdown の処理系によっては HTML 上で `|` ではなく `\|` になって壊れることがあります。",
    )
    if '</a>' not in msg:
        error_by_regex(
            pattern=r'\$.*[<>].*\$',
            text=r"KaTeX: 数式中では `<` や `>` ではなく `\lt` や `gt` や `\langle` や `\rangle` を使ってください。`<` や `>` は HTML のタグと解釈されて壊れることがあります。",
        )

    users = list_defined_users()
    for m in re.finditer(r'<a +class="handle">(\w+)</a>', msg):
        user = m.group(1)
        if user not in users:
            text = r'AtCoder ID: AtCoder ユーザー "{}" の色の情報がありません。`$ python3 scripts/user-ratings.py` を実行して色の情報のファイルを更新してください。'.format(user)
            result.append(error(text, file=path, line=line, col=m.start() + 1))

    warning_by_regex(
        pattern=r'捜査',
        text=r"typo: `捜査` ではなく `走査` の可能性があります。",
    )
    error_by_regex(
        pattern=r'[舐な]め[てる]',
        text=r"日本語: `舐める` ではなく `走査する` を使ってください。`舐める` はすこし informal であり、また `走査する` で置き換えても不都合はないはずです。",
    )

    if 'データ構造をマージする一般的なテク' not in msg:
        warning_by_regex(
            pattern=r'[^ァ-ヺ]テク[^ニ]',
            text=r"日本語: `データ構造をマージする一般的なテク` のような固有名詞の一部でない場合は、`テク` ではなく `テクニック` や `アルゴリズム` を使ってください。`テク` は informal すぎます。",
        )

    error_by_regex(
        pattern=r'多項式補完',
        text=r"typo: `多項式補完` ではなく `多項式補間` です。",
    )
    error_by_regex(
        pattern=r'補完多項式',
        text=r"typo: `補完多項式` ではなく `補間多項式` です。",
    )
    error_by_regex(
        pattern=r'[Ll]agrange *補完',
        text=r"typo: `Lagrange 補完` ではなく `Lagrange 補間` です。",
    )
    warning_by_regex(
        pattern=r'補完',
        text=r"typo: `補完` ではなく `補間` の可能性があります。",
    )

    for suffix in ['グラフ', '辺', '木', '閉路', '路']:
        error_by_regex(
            pattern=r'無効{}'.format(suffix),
            text=r"typo: `無効{}` ではなく `無向{}` です。".format(suffix, suffix),
        )
        error_by_regex(
            pattern=r'有効{}'.format(suffix),
            text=r"typo: `有効{}` ではなく `有向{}` です。".format(suffix, suffix),
        )

    warning_by_regex(
        pattern=r'組み合わせ(に|を|は|が|い|の|と|で)',
        text=r"typo: `組み合わせ` ではなく `組合せ` の可能性があります。",
    )
    warning_by_regex(
        pattern=r'組合せ(た|て|る|ない|ず|よう)',
        text=r"typo: `組合せ` ではなく `組み合わせ` の可能性があります。",
    )

    error_by_regex(
        pattern=r'\$\w *\\to *\w\$ *最短経路',
        text=r"style: `$s \to t$ 最短経路` ではなく `$s$-$t$ 最短経路` と書いてください。(https://github.com/kmyk/algorithm-encyclopedia/pull/43)",
    )
    error_by_regex(
        pattern=r'辺 *\$\w *\\to *\w\$',
        text=r"style: `有向辺 $x \to y$` ではなく `有向辺 $(x, y)$` と書いてください。(https://github.com/kmyk/algorithm-encyclopedia/pull/44)",
    )
    error_by_regex(
        pattern=r'辺 *\$\w *\$? *- *\$? *\w\$',
        text=r"style: `無向辺 $x - y$` ではなく `無向辺 $\lbrace x, y \rbrace$` と書いてください。(https://github.com/kmyk/algorithm-encyclopedia/pull/44)",
    )

    return result


def collect_messages_from_yaml_frontmatter(frontmatter: Dict[str, Any], *, path: pathlib.Path) -> Iterator[Message]:
    required_keys = [
        'layout',
        'authors',
        'reviewers',
        'date',
        'updated_at',
        'description',
    ]
    for key in required_keys:
        if key not in frontmatter:
            yield error('YAML frontmatter: `{}` を設定してください。'.format(key), file=path, line=-1, col=-1)
            return
        text = frontmatter[key]
        if isinstance(text, str) and text.startswith('${') and text.endswith('}'):
            yield error('YAML frontmatter: `{}` を編集してください。'.format(key), file=path, line=-1, col=-1)

    # metadata
    if frontmatter.get('layout') != 'entry':
        yield error('YAML frontmatter: `layout` には `entry` を設定してください。', file=path, line=-1, col=-1)
    if not frontmatter.get('draft') and not frontmatter.get('authors'):
        yield error('YAML frontmatter: `authors` を設定してください。', file=path, line=-1, col=-1)
    if not isinstance(frontmatter.get('date'), datetime.datetime):
        yield error('YAML frontmatter: `date` には ISO-8601 で編集時刻を設定してください。', file=path, line=-1, col=-1)

    # for _algorithm/*.py
    if '_algorithm' in str(path):
        if 'algorithm' not in frontmatter:
            yield error('YAML frontmatter: `algorithm` を設定してください。', file=path, line=-1, col=-1)
        if not isinstance(frontmatter.get('algorithm'), dict):
            yield error('YAML frontmatter: `algorithm` は辞書であるべきです。', file=path, line=-1, col=-1)
            return
        required_algorithm_keys = [
            'input',
            'output',
            'time_complexity',
            'space_complexity',
            'aliases',
            'level',
        ]
        for key in required_algorithm_keys:
            if key not in frontmatter['algorithm']:
                yield error('YAML frontmatter: `algorithm` の中に `{}` を設定してください。'.format(key), file=path, line=-1, col=-1)
                return
            text = frontmatter['algorithm'][key]
            if isinstance(text, str) and text.startswith('${') and text.endswith('}'):
                yield error('YAML frontmatter: `{}` を編集してください。'.format(key), file=path, line=-1, col=-1)

    # description
    if not frontmatter.get('description'):
        yield error('YAML frontmatter: `description` を記述してください。', file=path, line=-1, col=-1)
    yield from collect_messages_from_line(frontmatter['description'] or '', path=path, line=-1)

    # draft
    if frontmatter.get('draft'):
        if 'draft_urls' not in frontmatter:
            yield error('YAML frontmatter: 概要のみの記事には `draft_urls` を設定してください。', file=path, line=-1, col=-1)


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

    if not lines[-1].endswith('\n'):
        yield error('file: ファイルの末尾には改行文字を付与してください。テキストファイルとは行を並べたものであり、行とは改行文字で終了するものです。実用的には、commit log に不要な修正が紛れ込むことを防ぐ効果があります。', file=path, line=len(lines), col=len(lines[-1]))
    for i, line in enumerate(lines):
        if line.rstrip('\n').endswith(' '):
            yield error('file: 行の末尾の空白文字は削除してください。また、Markdown の強制改行は使わないでください。', file=path, line=i + 1, col=len(line))


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
