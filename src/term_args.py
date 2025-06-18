""" Single function just to parse CLI args """

import sys
import argparse

from _version import __version__

def term_args() -> argparse.Namespace:
    """
    Analyzes sys.argv to map the text to options.

    Parameters
    ----------
    None

    Returns
    -------
    term args : argparse.Namespace
                C struct in python where each member is an option. 
    """

    # NO ARGUMENTS
    if len(sys.argv) == 1:
        print(
            "What video manual do you want?\n"
            "For example, try 'vman ls'."
        )
        sys.exit(0)

    parser = argparse.ArgumentParser(
        prog="vman",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='%(prog)s [video] [options]',
        description="vman - Video Man Pages"
    )

    parser.add_argument(
        '-v','--version',
        action='version',
        version=f"""
%(prog)s v{__version__}
Copyright (C) 2025 Sivefunc
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human"""
    )

    parser.add_argument(
        'video',
        help="Video to consult in the video manual, e.g 'ls'",
        type=str,
        nargs="?",
        metavar="[VIDEO]"
    )

    parser.add_argument(
        '--urls',
        help="List all the video manuals in JSON format",
        action='store_true',
    )

    parser.add_argument(
        '-p',
        '--player',
        help="Path to media player to use instead of relying by default on xdg-open",
        type=str,
        metavar="PATH"
    )

    args = parser.parse_args()

    if not args.video and not args.urls:
        print('No video provided to play')
        sys.exit(1)

    return args
