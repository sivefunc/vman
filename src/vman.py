import os
import json
import shlex
import subprocess

from _version import __version__
from utils import (
    load_config,
    load_urls
)

import term_args

CONFIG = load_config()
DEFAULT_MEDIA_PLAYER = CONFIG['constants']['DEFAULT_MEDIA_PLAYER']

def main():
    t_args = term_args.term_args()

    if not t_args.video and not t_args.urls:
        print('No video provided to play')
        exit(1)

    urls = load_urls()

    if t_args.urls:
        print(json.dumps(urls, indent=4))
        exit(0)

    try:
        url = urls[t_args.video]

    except KeyError:
        print(f"No video manual for {t_args.video}")
        exit(16)

    media_player = DEFAULT_MEDIA_PLAYER if not t_args.player else t_args.player
    subprocess.run(shlex.split(f"{media_player} '{url}'"), check=True)

if __name__ == '__main__':
    main()
