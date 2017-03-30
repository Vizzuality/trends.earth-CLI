"""Create command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from shutil import copytree


def is_valid(name):
    """Check if the name is valid"""
    return bool(name)


def run():
    """Create command"""
    name = None
    while name is None or not is_valid(name):
        name = input("Please enter the project name: ")

    try:
        to_dir = os.getcwd() + '/' + name
        from_dir = os.path.dirname(os.path.realpath(__file__)) + '/skeleton'

        copytree(from_dir, to_dir)
    except Exception as error:
        raise

    return 'Project %s created successfully' % (name)
