# GEF CLI

This project belongs to the GEF Project.

This repo implements the CLI of the GEF Environment. It allows to create and test custom scripts locally. It also can be used to publish the scripts to the GEF Environment

Check out the other parts of the GEF project:

- The API [GEF API](https://github.com/Vizzuality/GEF-API)
- The GEF core platform [GEF Environment](https://github.com/Vizzuality/GEF-Environment)
- A web app to explore and manage the API entities [GEF UI](https://github.com/Vizzuality/GEF-UI)

## Getting started

### Requirements

- Python 3 [Python](https://www.python.org/)
- pip (pip3). Check the version ```pip -V```
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

Now you can use the CLI.

## Commands

### Create

To create a new script.
The program will ask for a non-existing name.

```
python gefcli create
```

### Start

To run a script locally.
First, go to the folder where the script has been created and run

```
python (relativepath) start
```

For instance:

```
python ../../gefcli start
python ../gefcli start
```

### Config
### Login
### Publish
### Download
### Clear
### Info
### Logs
