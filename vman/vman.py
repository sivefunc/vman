""" Entry point """

import sys
import json
import traceback

from ._version import __version__

from . import constants
from . import term_args
from .utils import (
    load_config_or_exit,
    get_urls_path_or_exit,
    load_urls_or_exit,
    get_video_url_or_exit,
    get_author_or_exit,
    get_author_urls_or_exit,
    get_media_player_or_exit,
    play_video
)

def main():
    """ Entry Point Function """
    try:
        t_args = term_args.term_args()
        config = load_config_or_exit()
        urls_path = get_urls_path_or_exit(config)
        urls = load_urls_or_exit(urls_path)
            
        if t_args.urls:
            print(json.dumps(urls, indent=4))
            sys.exit(constants.SUCCESS)

        author = get_author_or_exit(t_args.author, config.get('author'))
        author_urls = get_author_urls_or_exit(author, urls)
        video_url = get_video_url_or_exit(t_args.video, author, author_urls)

        if t_args.only_url:
            print(video_url)
            sys.exit(constants.SUCCESS)

        media_player = get_media_player_or_exit(t_args.player,
                                                config.get('media_player'))
        play_video(media_player, video_url)

    except KeyboardInterrupt:
        sys.exit(constants.USER_ERROR)

    except Exception:
        traceback.print_exc()
        sys.exit(constants.OPERATIONAL_ERROR)

    sys.exit(constants.SUCCESS)

if __name__ == '__main__':
    main()
