from flask import Flask
from flask_pagedown import PageDown
import jinja2

from config import Config, template_location, static_location

app = Flask(__name__, static_folder=static_location)
app.config.from_object(Config)
pagedown = PageDown(app)

loader = jinja2.ChoiceLoader([app.jinja_loader, jinja2.FileSystemLoader(template_location)])
app.jinja_loader = loader

from server import routes

