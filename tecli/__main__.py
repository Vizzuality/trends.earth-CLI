"""The GEF CLI Main."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

if __package__ == '':
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

import tecli

if __name__ == '__main__':
    sys.exit(tecli.main())
