import sys

from _version import __version__

import constants
import term_args
from utils import (
    load_config,
    get_urls_path,
    load_urls,
    get_video_url,
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

    video_url = get_video_url(t_args.video, urls)

    media_player = t_args.player if t_args.player else config['media_player']
    play_video(media_player, video_url)

if __name__ == '__main__':
    main()
