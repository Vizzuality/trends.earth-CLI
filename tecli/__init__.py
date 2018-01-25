"""The GEF CLI Module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

import fire
from tecli.commands import Commands

logging.basicConfig(
    level='DEBUG',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)


def main():
    """Create the CLI"""
    fire.Fire(Commands)
