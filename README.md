# FantasyTimeTracker
Time Tracking tool for tabletop roleplaying games

## Setup
* Make sure Python 3, pip and venv are installed
* Create Python 3 virtual environment for the program.
  ```python3 -m venv path/to/venv```
* Activate the virtual enviroment
  ```. ./path/to/venv/Scripts/activate```
* Install the dependency libraries with pip

```
pip install flask
pip install flask_wtf
pip install flask_pagedown
pip install markdown
pip install wtforms
pip install mdx_truly_sane_lists
```

* Deactivate the venv
  ```deactivate```

Other than Python 3, pip and venv setup, this step can be completed on windows
with setup.ps1 or on unix with setup.sh. The scripts create a folder for venv
in the folder they are run from.

## Running the server
* Set either production or development environment in the config.py
* Set environment variables FLASK_ENV and FLASK_DEBUG to match production or
  development option in config.py
* Set secret keys in config.py to random strings only you know
* Activate the virtual environment
```. ./path/to/venv/Scrips/activate```
* Run python flask
```python -m flask run```
* Open browser of your choice on address displayed
