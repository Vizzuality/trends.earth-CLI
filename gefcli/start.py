"""Create command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tempfile
import os
import subprocess
import time

from shutil import copytree
from shutil import copyfile


def buildDocker(tempdir, id):
    try:

        subprocess.run("docker build -t {0} .".format(id), shell=True, check=True, cwd=tempdir)
        return True
    except subprocess.CalledProcessError as error:
        print(error)
        return False

def runDocker(tempdir, id, param):
    try:
        subprocess.run("docker run --rm {0} {1}".format(id, param), shell=True, check=True, cwd=tempdir)
        return True
    except subprocess.CalledProcessError as error:
        print(error)
        return False

def run(param):
    """Start command"""
    print('Creating temporary file...')
    cwd = os.getcwd()
    dockerfile = os.path.dirname(os.path.realpath(__file__)) + '/run/Dockerfile'
    with tempfile.TemporaryDirectory() as tmpdirname:
        print('Copying files in ' + tmpdirname)
        print('Copying Dockerfile ....')
        copyfile(dockerfile, tmpdirname + '/Dockerfile' )
        print('Copying src folder ....')
        copytree(cwd + '/src', tmpdirname + '/src')
        print('Copying requirements ....')
        copyfile(cwd + '/requirements.txt', tmpdirname + '/requirements.txt')
        print('Do building ....')
        id = time.time()
        if buildDocker(tmpdirname, id):
            print('Running script ....')
            runDocker(tmpdirname, id, param)



    return param
