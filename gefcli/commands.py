"""Wrapper for the CLI commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from gefcli import create
from gefcli import start


class Commands(object):
    """GEF Command class Wrapper"""

    @staticmethod
    def create():
        """Create new project"""
        return create.run()

    @staticmethod
    def start(param):
        """Start a script"""
        return start.run(param)

    @staticmethod
    def config():
        """Config GEE"""
        return "config"

    @staticmethod
    def login():
        """Log in the API"""
        return "login"

    @staticmethod
    def publish():
        """Publish a script"""
        return "publish"

    @staticmethod
    def download():
        """Download a script"""
        return "download"

    @staticmethod
    def clear():
        """Clear docker trash"""
        return "clear"
