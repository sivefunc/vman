import json
import os
import pathlib

import sys

from _version import __version__

def get_url(urls: dict) -> list[bool, str]:
    try:
        result = [True, urls[sys.argv[1]]]
    
    except IndexError:
        result = [False, "No video Provided"]

    except KeyError:
        result = [False, f"Video for '{sys.argv[1]}' does not exist"]

    return result

def main():
    urls_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        'urls.json'
    )

    with open(urls_path, 'r') as json_fp:
        urls = json.load(json_fp)

    success, url = get_url(urls)
    if not success:
        print(url)
        exit()

    print(__version__)
    print(url)

if __name__ == '__main__':
    main()

