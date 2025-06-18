import os
import sys
import json
import shlex
import pathlib
import subprocess

from _version import __version__
from utils import (
    load_config,
    load_urls
)

import term_args

SRC_PATH = pathlib.Path(__file__).parent.resolve()
CONFIG_PATH = os.path.join(SRC_PATH, 'config.toml')

def main():
    config = load_config(CONFIG_PATH)

    t_args = term_args.term_args()

    urls_path = os.path.join(SRC_PATH, 'urls.json')
    if config['custom-urls']['enabled']:
        urls_path = config['custom-urls']['path']

    urls = load_urls(urls_path)
    
    if t_args.urls:
        print(json.dumps(urls, indent=4))
        sys.exit(0)

    try:
        url = urls[t_args.video]

    except KeyError:
        print(f"No video manual for {t_args.video}")
        sys.exit(16)

    media_player = config['media_player']
    if t_args.player:
        media_player = t_args.player

    subprocess.run(shlex.split(f"{media_player} '{url}'"), check=True)

if __name__ == '__main__':
    main()
