import json
import os
import pathlib

from _version import __version__

def main():
    urls_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        'urls.json'
    )

    with open(urls_path, 'r') as json_fp:
        urls = json.load(json_fp)

    print(__version__)
    print(urls)

if __name__ == '__main__':
    main()

