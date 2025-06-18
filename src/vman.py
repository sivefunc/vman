import os
import sys
import json
import shlex
import tomllib
import subprocess

from _version import __version__

import constants
import term_args

def main():

    # Config Loading
    try:
        with open(constants.CONFIG_PATH, 'rb') as config_fp:
            config = tomllib.load(config_fp)

    except FileNotFoundError:
        print(f"vman configuration file does not exist at: "
              f"'{constants.CONFIG_PATH}'")
        exit(constants.USER_ERROR)

    except tomllib.TOMLDecodeError as parsing_error:
        print(f"error parsing vman config file at: '{constants.CONFIG_PATH}'"
              f"\n{parsing_error}")
        exit(constants.USER_ERROR)

    t_args = term_args.term_args()

    urls_path = os.path.join(constants.SRC_PATH, 'urls.json')
    if (config.get('custom-urls') is not None
            and config['custom-urls'].get('enabled')):

        try:
            urls_path = config['custom-urls']['path']

        except KeyError:
            print(f"[custom-urls] is enabled at: '{constants.CONFIG_PATH}'"
                  " " "but a path was not given, it should be like this:"
                  "\n[custom-urls]"
                  "\nenabled = true"
                  "\npath = '/home/user-name/.config/vman/urls.json'"
                  )

    # Load URL's JSON File
    try:
        with open(urls_path, 'r') as json_fp:
            urls = json.load(json_fp)
    
    except FileNotFoundError:
        print(f"vman urls json file does not exist at: "
              f"'{urls_path}'")
        exit(constants.USER_ERROR)

    except json.JSONDecodeError as parsing_error:
        print(f"error parsing vman urls json file at: '{urls_path}'"
              f"\n{parsing_error}")
        exit(constants.USER_ERROR)
    
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
