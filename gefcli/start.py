"""Create command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tempfile
import os
import subprocess
import time
import logging

from shutil import copytree, copyfile


def build_docker(tempdir, dockerid):
    """Build docker"""
    try:
        subprocess.run("docker build -t {0} .".format(dockerid), shell=True, check=True, cwd=tempdir)
        return True
    except subprocess.CalledProcessError as error:
        logging.error(error)
        return False


def run_docker(tempdir, dockerid, param):
    """Run docker"""
    try:
        subprocess.run("docker run --rm {0} {1}".format(dockerid, param), shell=True, check=True, cwd=tempdir)
        return True
    except subprocess.CalledProcessError as error:
        logging.error(error)
        return False


def run(param):
    """Start command"""
    logging.debug('Creating temporary file...')
    # Current folder
    cwd = os.getcwd()
    # Getting Dockerfile from /run folder
    dockerfile = os.path.dirname(os.path.realpath(__file__)) + '/run/Dockerfile'

    with tempfile.TemporaryDirectory() as tmpdirname:
        logging.debug('Copying Dockerfile ...')
        copyfile(dockerfile, tmpdirname + '/Dockerfile')

        logging.debug('Copying src folder ...')
        copytree(cwd + '/src', tmpdirname + '/src')

        logging.debug('Copying requirements ...')
        copyfile(cwd + '/requirements.txt', tmpdirname + '/requirements.txt')

        logging.debug('Building ...')
        dockerid = time.time()
        if build_docker(tmpdirname, dockerid):
            print('Running script ....')
            run_docker(tmpdirname, dockerid, param)
