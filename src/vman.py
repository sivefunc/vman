import sys

from _version import __version__

import constants
import term_args
from utils import (
    load_config,
    get_urls_path,
    load_urls,
    get_video_url,
    get_author,
    get_author_urls,
    get_media_player,
    play_video
)

def main():
    t_args = term_args.term_args()
    config = load_config()
    urls_path = get_urls_path(config)
    urls = load_urls(urls_path)
        
    if t_args.urls:
        print(json.dumps(urls, indent=4))
        sys.exit(constants.SUCCESS)

    author = get_author(t_args.author, config.get('author'))
    author_urls = get_author_urls(author, urls)
    video_url = get_video_url(t_args.video, author, author_urls)
    media_player = get_media_player(t_args.player, config.get('media_player'))
    play_video(media_player, video_url)

if __name__ == '__main__':
    main()
