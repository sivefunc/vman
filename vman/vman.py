""" Entry point """

# Standard Library
import sys
import json
import traceback

# Local
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
        terminal = term_args.term_args()

        # Loading Files
        config = load_config_or_exit()
        urls_path = get_urls_path_or_exit(config)
        urls = load_urls_or_exit(urls_path)
            
        # Print all the Urls
        if terminal.urls:
            print(json.dumps(urls, indent=4))
            sys.exit(constants.SUCCESS)

        # Get Video made by Author
        author = get_author_or_exit(terminal.author, config.get('author'))
        author_urls = get_author_urls_or_exit(author, urls)
        video_url = get_video_url_or_exit(terminal.video, author, author_urls)

        # Print only the video url
        if terminal.only_url:
            print(video_url)
            sys.exit(constants.SUCCESS)

        # Play the video
        media_player = get_media_player_or_exit(terminal.player,
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
