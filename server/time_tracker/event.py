
class Event:
    def __init__(self, characters, start, length, action):
        # List of characters involved
        self.characters = characters
        # Number of smallest units from epoch to start of the event
        self.start = start
        # Number of the smallest units this event took
        self.length = length
        # Time of the end of the event
        self.end = start + length
        # String describing the event
        self.description = action

    def __str__(self):
        string = ""
        string += self.calendar.get_time(start)
