#!/usr/bin/env python3
import argparse
import json
import pathlib
import re
import time
import urllib.request
from logging import DEBUG, basicConfig, getLogger
from typing import *

logger = getLogger(__name__)


def download_rating_value(user: str) -> Optional[int]:
    url = 'https://atcoder.jp/users/{}/history/json'.format(user)
    time.sleep(1)
    logger.info('GET %s', url)
    try:
        with urllib.request.urlopen(url) as fh:
            data = json.load(fh)
    except Exception:
        logger.exception('failed to load the history json: user = %s', repr(user))
        return None
    if not data:
        return -1
    rating = 0
    for row in data:
        rating = max(rating, row['NewRating'])
    return rating


def get_rating_color_from_value(rating: int) -> str:
    if rating < 0:
        return 'black'
    elif rating < 400:
        return 'grey'
    elif rating < 800:
        return 'brown'
    elif rating < 1200:
        return 'green'
    elif rating < 1600:
        return 'cyan'
    elif rating < 2000:
        return 'blue'
    elif rating < 2400:
        return 'yellow'
    elif rating < 2800:
        return 'orange'
    else:
        return 'red'


def collect_users(*, basedir: pathlib.Path) -> List[str]:
    users: List[str] = []
    for path in basedir.glob('**/*.md'):
        if path.name == 'template.md':
            continue
        with open(path) as fh:
            for line in fh.readlines():
                if line.lstrip().startswith('authors:'):
                    users.extend(re.findall(r'\w+', line)[1:])
                if line.lstrip().startswith('reviewers:'):
                    users.extend(re.findall(r'\w+', line)[1:])
                users.extend(re.findall(r'<a class="handle">(\w+)</a>', line))
    return sorted(set(users))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=pathlib.Path, default=pathlib.Path.cwd())
    parser.add_argument('--output', type=pathlib.Path, default=pathlib.Path('_sass', 'user-colors.scss'))
    args = parser.parse_args()
    basicConfig(level=DEBUG)

    lines = []
    lines.append('// THIS FILE IS GENERATED BY user-ratings.py! DO NOT EDIT!')
    lines.append('@import "rating-colors";')
    lines.append('.handle { font-weight: bold; }')
    users = collect_users(basedir=args.input)
    for user in users:
        rating = download_rating_value(user)
        if rating is None:
            continue
        color = get_rating_color_from_value(rating)
        logger.info('user-%s -> %s', user, color)
        lines.append('.user-{} {{ color: $rating-color-{}; }}'.format(user, color))
    with open(args.output, 'w') as fh:
        for line in lines:
            print(line, file=fh)


if __name__ == '__main__':
    main()
