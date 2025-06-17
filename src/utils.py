import os
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
