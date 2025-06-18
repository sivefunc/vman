""" Functions used in vman.py

The majority of these functions comes in the form 'execute_or_exit(...)'
indicating that if some function fails the program will sys.exit(...).
"""

import os
import sys
import json
import shlex
import tomllib
import subprocess

from . import constants

def load_config_or_exit():
    try:
        with open(constants.CONFIG_PATH, 'rb') as config_fp:
            config = tomllib.load(config_fp)

    except FileNotFoundError:
        print(f"vman configuration file does not exist at: "
              f"'{constants.CONFIG_PATH}'")
        sys.exit(constants.USER_ERROR)

    except tomllib.TOMLDecodeError as parsing_error:
        print(f"error parsing vman config file at: '{constants.CONFIG_PATH}'"
              f"\n{parsing_error}")
        sys.exit(constants.USER_ERROR)
    
    return config

def get_urls_path_or_exit(config):
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
            sys.exit(constants.USER_ERROR)

    return urls_path

def get_author_or_exit(author_args, author_config):
    author = author_args
    if author is None:
        if author_config is not None:
            author = author_config

        else:
            print(f"error parsing vman config file at:"
                    " " f"'{constants.CONFIG_PATH}'"
                  "\nconfig file does not have a default author"
                  "\ne.g: author = 'distrotube'")
            sys.exit(constants.USER_ERROR)

    return author

def load_urls_or_exit(urls_path):
    try:
        with open(urls_path, 'r') as json_fp:
            urls = json.load(json_fp)
    
    except FileNotFoundError:
        print(f"vman urls json file does not exist at: "
              f"'{urls_path}'")
        sys.exit(constants.USER_ERROR)

    except json.JSONDecodeError as parsing_error:
        print(f"error parsing vman urls json file at: '{urls_path}'"
              f"\n{parsing_error}")
        sys.exit(constants.USER_ERROR)

    return urls

def get_author_urls_or_exit(author, urls):
    try:
        author_urls = urls[author]

    except KeyError:
        print(f"The author '{author}' does not exist")
        sys.exit(constants.NO_AUTHOR_ERROR)

    return author_urls

def get_media_player_or_exit(media_player_terminal, media_player_config):
    media_player = media_player_terminal
    if media_player is None:
        if media_player_config is not None:
            media_player = media_player_config

        else:
            print(f"error parsing vman config file at:"
                    " " f"'{constants.CONFIG_PATH}'"
                  "\nconfig file does not have a default media player"
                  "\ne.g: media_player = 'xdg-open'")
            sys.exit(constants.USER_ERROR)

    return media_player

def get_video_url_or_exit(video, author, author_urls):
    try:
        video_url = author_urls[video]

    except KeyError:
        print(f"The author '{author}' does not have a manual about '{video}'")
        sys.exit(constants.NO_VIDEO_MANUAL_ERROR)

    return video_url

def play_video(media_player, video_url):
    subprocess.run(shlex.split(f"{media_player} '{video_url}'"), check=True)
