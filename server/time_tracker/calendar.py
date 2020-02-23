from server.time_tracker.month import Month, months

def getDaysIn(month):
    return months[month].length

def getNextMonth(month, year):
    if i < len(months) - 1:
        return i+1, year
    else:
        return 0, year + 1

def getMonthName(index):
    return months[index]

def getWeekdays():
    weekdays = ["Niram", "Doriav", "Amula", "Libetu", "Eheina", "Syrik"]
    return weekdays;

def getWeekday(index):
    return getWeekdays()[index]

def getMinuteTicks():
    return 60

def getHourTicks():
    return 60 * getMinuteTicks

def getDayTicks():
    return 24 * getHourTicks()

def getMonthTicks(index):
    return getDayTicks() * getDaysIn(index)

def getYearTicks():
    return sum([getMonthTicks(index) for index in range(len(months))])

class Calendar:
    def __init__(self, epoch, lengths):
        # Map of unit -> value at epoch
        self.epoch = epoch;
        # Map of unit -> (smaller unit, number needed for this unit)
        self.events = []

    def timestamp(self, date):
        time = 0;

    def addEvent(event):
        self.events.append(event)
        self.events.sort(key=lambda event: event.start)


    def getDate(self, stamp):
        year = epoch.year
        year += stamp // self.yearlength
        stamp = stamp % self.yearlenth
        
        month = epoch.month
        while(stamp > months[month].length * self.day):
            stamp -= months[month].length * self.day
            month +=1
            if month >= len(months):
                year += 1
                month = 0

        day = epoch.day
        day += stamp / day

    def getWeekday(self, stamp):
        dayCount = stamp // self.dayTicks
        start = self.epoch.weekday
        return weekdays[(start + dayCount) % len(weekdays)]

    def getYear(self, stamp):
        self.epoch.year + stamp // yearTicks;

