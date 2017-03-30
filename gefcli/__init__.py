"""The GEF CLI Module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import fire
from gefcli.commands import Commands


def main():
    """Create the CLI"""
    fire.Fire(Commands)
