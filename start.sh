#!/bin/zsh

source venv/bin/activate
export FLASK_APP=run.py
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run
deactivate
