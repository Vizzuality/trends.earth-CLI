from shutil import copytree
import os

class Commands(object):
    """A simple calculator class."""

    def create(self, name):
        """Create new project"""
        to_dir = os.getcwd() + '/' + name
        from_dir = os.path.dirname(os.path.realpath(__file__)) + '/skeleton'

        copytree(from_dir, to_dir)
        return 'Project %s created successfully'%(name)

    def start(self, param):
        return "start"

    def config(self):
        return "config"

    def login(self):
        return "login"
    
    def publish(self):
        return "publish"

    def download(self):
        return "download"
