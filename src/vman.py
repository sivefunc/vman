import os
import json
import shlex
import pathlib
import subprocess

from _version import __version__
import term_args

DEFAULT_MEDIA_PLAYER = "xdg-open"

def main():
    t_args = term_args.term_args()
    if not t_args.video and not t_args.urls:
        print('No video provided to play')
        exit(1)

    urls_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        'urls.json'
    )

    with open(urls_path, 'r') as json_fp:
        urls = json.load(json_fp)

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

