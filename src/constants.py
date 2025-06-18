import os
import pathlib

# Paths
SRC_PATH = pathlib.Path(__file__).parent.resolve()
CONFIG_PATH = os.path.join(SRC_PATH, 'config.toml')

# Return codes
SUCCESS                 = 0
USER_ERROR              = 1
OPERATIONAL_ERROR       = 2
CHILD_ERROR             = 3
NO_VIDEO_MANUAL_ERROR   = 16
