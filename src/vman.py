import os
import sys
import json
import shlex
import subprocess

from _version import __version__
from utils import (
    load_config,
    load_urls
)

import constants
import term_args

def main():
    config = load_config(constants.CONFIG_PATH)

    t_args = term_args.term_args()

    urls_path = os.path.join(constants.SRC_PATH, 'urls.json')
    if config['custom-urls']['enabled']:
        urls_path = config['custom-urls']['path']

    urls = load_urls(urls_path)
    
    if t_args.urls:
        print(json.dumps(urls, indent=4))
        sys.exit(constants.SUCCESS)

    try:
        url = urls[t_args.video]

    except KeyError:
        print(f"No video manual for {t_args.video}")
        sys.exit(constants.NO_VIDEO_MANUAL_ERROR)

    media_player = config['media_player']
    if t_args.player:
        media_player = t_args.player

    subprocess.run(shlex.split(f"{media_player} '{url}'"), check=True)

if __name__ == '__main__':
    main()
