import os
import sys

# This file adjusts the path in order to import the main package even
# though we are in the test path, and then imports the main package
# into this 'context', so that modules in the main package can be
# imported in tests with the following:
#
# from .context import picpick
# import pickpick.somemodule

sys.path.insert(0, os.path.abspath('..'))

import picpick
