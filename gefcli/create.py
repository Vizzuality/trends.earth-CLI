from shutil import copytree
import os

def run():
    name = input("Please enter the project name: ")

    to_dir = os.getcwd() + '/' + name
    from_dir = os.path.dirname(os.path.realpath(__file__)) + '/skeleton'

    copytree(from_dir, to_dir)

    return 'Project %s created successfully'%(name)
