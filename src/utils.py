import os
import json
import tomllib
import pathlib

def load_config():
    config_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        'config.toml'
    )

    with open(config_path, 'rb') as config_fp:
        config = tomllib.load(config_fp)

    return config

def load_urls():
    urls_path = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        'urls.json'
    )

    with open(urls_path, 'r') as json_fp:
        urls = json.load(json_fp)

    return urls
