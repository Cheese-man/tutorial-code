# COMP6843 25t1
I'll put sample code/notes here throughout the term :)

## Some general stuff

### Python virtual environments
To set up a virtual environment with Python, run the following commands in the folder you want to keep your scripts in:
```sh
python3 -m venv .venv 
# (you can replace .venv with whatever you like, it'll create a directory with that name)
source .venv/bin/activate 
# (replace '.venv' with whatever you named the directory in the first step)
```

Then, run `pip install` to install the requests library (and/or any other libraries you like):
```sh
pip install requests
```