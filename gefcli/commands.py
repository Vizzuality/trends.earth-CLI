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
            print('Creating the project')
            if create.run():
                print('Project created successfully')
            else:
                print('Project not created')
        except Exception as error:
            logging.error(error)

    @staticmethod
    def start(param={}):
        """Start a script"""
        try:
            print('Running the script')
            if start.run(param):
                print('Execution Finished')
            else:
                print('Error running the script')
        except Exception as error:
            logging.error(error)

    @staticmethod
    def config(action, var_name, value=None):
        """Config GEE"""
        try:
            print('Configuring the script')
            if configuration.run(action, var_name, value):
                print('Configuration done')
            else:
                print('Error in the configuration')
        except Exception as error:
            logging.error(error)

    @staticmethod
    def login():
        """Log in the API"""
        try:
            print('Logging the user in')
            if login.run():
                print('You are logged')
            else:
                print('Error with the user')
        except Exception as error:
            logging.error(error)

    @staticmethod
    def publish():
        """Publish a script"""
        try:
            print('Publishing the script')
            if publish.run():
                print('Script published successfully')
            else:
                print('Error publishing the script')
        except Exception as error:
            logging.error(error)

    @staticmethod
    def download():
        """Download a script"""
        try:
            print('Downloading the script')
            if download.run():
                print('Script downloaded successfully')
            else:
                print('Error downloading the script')
        except Exception as error:
            logging.error(error)

    @staticmethod
    def clear():
        """Clear docker trash"""
        try:
            print('Cleaning trash')
            if clear.run():
                print('You are cleaned enough')
            else:
                print('Error cleaning the system')
        except Exception as error:
            logging.error(error)
