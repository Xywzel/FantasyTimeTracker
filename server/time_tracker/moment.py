from server.time_tracker.date import Date

class Moment(Date):
    def __init__(self, year, month, day, hour, minute, second):
        Date.__init__(self, year, month, day)
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "%d-%d-%d %d:%d:%d" % (self.year, self.month + 1, self.day + 1)

