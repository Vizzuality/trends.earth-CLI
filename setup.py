from setuptools import setup

setup(name='gef-cli',
      version='0.3.0',
      description='Library to interact with GEF',
      author='Sergio Gordillo, Raul Requero',
      author_email='sergio.gordillo@vizzuality.com,raul.requero@vizzuality.com',
      license='MIT',
      packages=['gefcli'],
      install_requires=[
          'fire'
      ],
      entry_points={
          "console_scripts": [
              "gef=gefcli:main"
          ]
      },
      zip_safe=False)
