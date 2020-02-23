from flask import render_template, redirect, request, url_for

from server import app
from server.time_tracker import get_time_tracker, get_time_viewer, set_time_tracker, advance_time_tracker

@app.route('/')
def index():
    return get_time_viewer()

@app.route('/time_viewer')
def time_viewer():
    return get_time_viewer()

@app.route('/time_tracker')
def time_tracker():
    return get_time_tracker()

@app.route('/time_tracker/<name>', methods=['POST'])
def time_tracker_value(name):
    value = request.form.get(name)
    set_time_tracker(name, value)
    return redirect(url_for('time_tracker'))

@app.route('/time_tracker/time', methods=['POST'])
def time_tracker_time():
    year = request.form.get('year')
    month = request.form.get('month')
    day = request.form.get('day')
    hour = request.form.get('hour')
    minute = request.form.get('minute')
    second = request.form.get('second')
    set_time_tracker('time', [year, month, day, hour, minute, second])
    return redirect(url_for('time_tracker'))

@app.route('/time_tracker/advance', methods=['POST'])
def time_tracker_advance():
    unit = request.form.get('unit')
    advance_time_tracker(unit)
    return redirect(url_for('time_tracker'))
