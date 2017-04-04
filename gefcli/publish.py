"""Publish command"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from termcolor import colored

from gefcli.configuration import SETTINGS

from gefcli import config

import tarfile
import logging
import os
import json
import requests


def make_tarfile(name):
    """Create tar.gz file with the content of the directory"""
    to_dir = os.getcwd()
    makefile = os.path.join(to_dir, name +'.tar.gz')
    logging.debug('Creating tar.gz file in path: %s' % (to_dir))
    with tarfile.open(makefile, "w:gz") as tar:
        tar.add(to_dir, arcname=os.path.basename(to_dir))
        return makefile

def read_configuration():
    """Read configuration file of project"""
    to_dir = os.getcwd()
    logging.debug('Reading configuration file in path: %s' % (to_dir))
    with open(os.path.join(to_dir, 'configuration.json'), 'r') as json_data:
        d = json.load(json_data)
        return d

def write_configuration(data):
    """Write configuration file"""
    to_dir = os.getcwd()
    logging.debug('Writting configuration file in path: %s' % (to_dir))
    with open(os.path.join(to_dir, 'configuration.json'), 'w') as config_file:
        json.dump(data, config_file)

def read_jwt_token():
    """Obtain jwt token of config user"""
    return config.get('JWT')


def publish():
    """Publish script in API"""
    tarfile = None
    try:
        configuration = read_configuration()
        if 'name' not in configuration:
            print('Name required in configuration file')
            return False
        tarfile = make_tarfile(configuration['name'])
        logging.debug('Doing request with file %s' %(tarfile))
        token = read_jwt_token()
        response = requests.post(url=SETTINGS.get('url_api')+'/api/v1/script', files={'file': open(tarfile, 'rb')}, headers={'Authorization': 'Bearer ' + token})

        if response.status_code != 200:
            logging.error(response.json())
            if response.status_code == 401:
                print(colored('Do you need login', 'red'))
            else:
                print(colored('Error publishing script.', 'red'))
            return False

        print(response)
        data = response.json()
        print (data)
        configuration['id']=response['id']
        write_configuration(configuration)
        return True
    except (OSError, IOError) as e:
        print(colored('Execute this command in a GEF project', 'red'))
        return False
    finally:
        if tarfile:
            os.remove(path=tarfile)


def run():
    """Publish command"""
    return publish()
