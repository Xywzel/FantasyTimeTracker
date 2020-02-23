import os
import json

from flask import render_template, send_file

from server.json import Encoder
from server.time_tracker.moment import Moment

def get_tracker_path():
    path = os.path.join(os.getcwd(), "data", "files", "time_tracker.json")
    return path

def get_time_tracker():
    tracker = TimeTracker(get_tracker_path())
    return render_template('time_tracker.html', track=tracker)

def get_time_viewer():
    tracker = TimeTracker(get_tracker_path())
    return render_template('time_viewer.html', track=tracker)

def set_time_tracker(variable, value):
    print("set", variable, "to", value)
    tracker = TimeTracker(get_tracker_path())
    tracker.set(variable, value)
    tracker.save()

def advance_time_tracker(unit):
    pass

class TimeTracker:
    def __init__(self, filename):
        self.filename = filename;
        self.time = Moment(0, 0, 0, 0, 0, 0)
        self.wind_speed = 0
        self.wind_dir = 0
        self.rain = 0
        self.clouds = "None"
        self.special = "None"
        self.background = "None"
        self.load()

    def set(self, variable, value):
        if (variable == "wind_speed"):
            self.wind_speed = int(value)
        elif (variable == "wind_dir"):
            self.wind_dir = value
        elif (variable == "rain"):
            self.rain = int(value)
        elif (variable == "clouds"):
            self.clouds = value
        elif (variable == "special"):
            self.special = value
        elif (variable == "background"):
            self.background = value
        elif (variable == "time"):
            self.time = Moment(value)

    def get_clouds(self):
        return ["none", "light", "half", "heavy"]

    def get_backgrounds(self):
        return ["plains","hills","forest","jungle","lake","sea","cave","dungeon","village","town"]

    def get_specials(self):
        return ["none", "thunder", "lightning", "meteors"]

    def get_directions(self):
        return ["n", "ne", "e", "se", "s", "sw", "w", "nw"]

    def get_time_units(self):
        return ["turn", "round", "minute", "hour", "long rest", "day", "week", "month", "year"]

    def get_months(self):
        return ["January", "Febuary"]

    def get_days(self):
        return range(1, 30)

    def save(self):
        filename = self.filename
        del self.filename
        data = json.dumps(self.__dict__)
        with open(filename, 'w', encoding="utf8") as f:
            f.write(data)

    def load(self):
        data = {}
        with open(self.filename, 'r', encoding="utf8") as f:
            data = json.load(f)
        self.__dict__.update(data)
