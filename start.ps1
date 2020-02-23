. .\venv\Scripts\activate
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = 1
python -m flask run
deactivate
