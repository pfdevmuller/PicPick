import os
import sys

# This file adjusts the path for tests, so that the packaged module can be
# imported in tests with the following:
# from .context import sample

sys.path.insert(0, os.path.abspath('..'))

import pickpick
