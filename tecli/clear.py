"""Clear command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import logging
import subprocess


def clear_unusued_docker():
    """Clear dockers"""
    try:
        subprocess.run("docker ps -a | awk '{ print $1,$2 }' | grep gef-local | awk '{print $1 }' | xargs -I {} docker rm -fv {}", shell=True, check=True, cwd=os.getcwd())
        subprocess.run("docker images -a | awk '{ print $1,$2 }' | grep gef-local | awk '{print $1 }' | xargs -I {} docker rmi {}", shell=True, check=True, cwd=os.getcwd())
        return True
    except subprocess.CalledProcessError as error:
        logging.error(error)
        return True


def run():
    """Clear command"""
    success = False
    if clear_unusued_docker():
        logging.debug('Cleaned up!')
        success = True

    return success
