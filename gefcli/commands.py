from __future__ import absolute_import
from gefcli import create
from gefcli import start

class Commands(object):
    """GEF cli"""

    def create(self):
        """Create new project"""
        return create.run()

    def start(self, param):
        return start.run(param)

    def config(self):
        return "config"

    def login(self):
        return "login"
    
    def publish(self):
        return "publish"

    def download(self):
        return "download"
