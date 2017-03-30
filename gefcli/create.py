"""Create command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from shutil import copytree


def run():
    """Create command"""
    name = input("Please enter the project name: ")

    to_dir = os.getcwd() + '/' + name
    from_dir = os.path.dirname(os.path.realpath(__file__)) + '/skeleton'

    copytree(from_dir, to_dir)

    return 'Project %s created successfully' % (name)
