import os
import json
import tomllib
import pathlib

def load_config(path: str):
    with open(path, 'rb') as config_fp:
        config = tomllib.load(config_fp)

    return config

def load_urls(path: str):
    with open(path, 'r') as json_fp:
        urls = json.load(json_fp)

    return urls
