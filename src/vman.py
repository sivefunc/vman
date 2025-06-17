import os
import json
import shlex
import pathlib
import subprocess

from _version import __version__
import term_args

def main():
    t_args = term_args.term_args()
    urls_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        'urls.json'
    )

    with open(urls_path, 'r') as json_fp:
        urls = json.load(json_fp)

    try:
        url = urls[t_args.video]

    except KeyError:
        print(f"No video manual for {t_args.video}")
        exit(16)

    subprocess.run(shlex.split(f"xdg-open '{url}'"), check=True)

if __name__ == '__main__':
    main()

