"""Clear command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess


def clear_unusued_docker():
    """Clear dockers"""
    try:
        subprocess.run("docker rmi $(docker images | grep 'gef-local-')", shell=True, check=True, cwd=os.getcwd())
        return True
    except subprocess.CalledProcessError as error:
        logging.error(error)
        return False


def run():
    """Clear command"""
    success = False
    if clear_unusued_docker():
        logging.debug('Cleaned up!')
        success = True

    return success
