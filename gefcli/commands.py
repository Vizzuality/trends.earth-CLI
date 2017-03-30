"""Wrapper for the CLI commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

from gefcli import create, start, config, login, publish, download, clear


class Commands(object):
    """GEF Command class Wrapper"""

    @staticmethod
    def create():
        """Create new project"""
        try:
            create.run()
        except Exception as error:
            logging.error(error)

    @staticmethod
    def start(param):
        """Start a script"""
        try:
            start.run(param)
        except Exception as error:
            raise error

    @staticmethod
    def config():
        """Config GEE"""
        try:
            config.run()
        except Exception as error:
            raise error

    @staticmethod
    def login():
        """Log in the API"""
        try:
            login.run()
        except Exception as error:
            raise error

    @staticmethod
    def publish():
        """Publish a script"""
        try:
            publish.run()
        except Exception as error:
            raise error

    @staticmethod
    def download():
        """Download a script"""
        try:
            download.run()
        except Exception as error:
            raise error

    @staticmethod
    def clear():
        """Clear docker trash"""
        try:
            clear.run()
        except Exception as error:
            raise error
