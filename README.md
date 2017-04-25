# GEF CLI

This project belongs to the GEF Project.

This repo implements the CLI of the GEF Environment. It allows to create and test custom scripts locally. It also can be used to publish the scripts to the GEF Environment

Check out the other parts of the GEF project:

- The API [GEF API](https://github.com/Vizzuality/GEF-API)
- The GEF core platform [GEF Environment](https://github.com/Vizzuality/GEF-Environment)
- A web app to explore and manage the API entities [GEF UI](https://github.com/Vizzuality/GEF-UI)

## Getting started

### Requirements

- Python 3 [Download Python](https://www.python.org/)
- pip (pip3). You can check the version you have installed doing ```pip -V```
- virtualenv. ```pip install virtualenv```

### Setup

- Clone the repo and go to the folder

```
git clone https://github.com/Vizzuality/GEF-CLI
cd GEF-CLI
```

- Create a virtual environment if you haven't already

```
virtualenv -p python3 venv
```

- Activate it (you should do this step any time you want to run the project locally)

```
source venv/bin/activate
```

- Install the dependencies

```
pip install -r requirements.txt
```

Now you can use the CLI commands

## Commands

### Create

To create a new script.
The program will ask you for a name of your script.

```
python gefcli create
```

### Start

To run a script locally.
First, go to the folder where the script has been created and run the following:

```
python (relativepath) start
```

For instance:

```
python ../../gefcli start
python ../gefcli start
```

### Config

To configure basic params like a GEE Account.

For EE_PRIVATE_KEY param it's neccesary set the value in base64 encode. To encode use the next command:

```
cat privatekey.pem | base64
```

```
python gefcli config set EE_SERVICE_ACCOUNT <value>
python gefcli config set EE_PRIVATE_KEY <base64value>
```

It is also possible to see the current config

```
python gefcli config show EE_SERVICE_ACCOUNT
python gefcli config show EE_PRIVATE_KEY
```

And even unset one or both of them

```
python gefcli config unset EE_SERVICE_ACCOUNT
python gefcli config unset EE_PRIVATE_KEY
```

### Login

To log in the API. This step is necessary when publishing scripts

```
python gefcli login
```

### Publish

This command allows the user to publish the script to prod. As it was said, it's required to be logged before
publish a script.

```
python gefcli publish
```

### Logs

To see the build logs printed by the script.

```
python gefcli logs
```

### Info

To see some basic info about the script

```
python gefcli info
```

### Clear

Not yet

### Download

Not yet

## Examples

### Tensorflow

It defines, trains and evaluates a simple perceptron model to identify handwritten digits from the MNIST dataset.

You can test the behavior doing the following:

```
python ../../gefcli start
```

### Numpy

This script just concatenates two numpy arrays. It also shows how to define a custom Python class.

### Google Earth Engine

It calculates the umd forest loss or gain based on a given area and a period of time.
