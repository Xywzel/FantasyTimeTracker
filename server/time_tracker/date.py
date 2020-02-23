from server.time_tracker.calendar import getDaysIn, getNextMonth

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.fix()

    def fix(self):
        while (self.day >= getDaysIn(self.month)):
            self.day -= getDaysIn(self.month)
            self.month, self.year = getNextMonth(self.month, self.year)

    def __str__(self):
        return "%d-%d-%d" % ()

