'''
    TimeEntry: An object that contains a date and time someone studied, what they studied, and how long they studied that subject.
'''
class TimeEntry:
    def __init__(self, datetime, time_studied, subject):
        self.datetime = datetime
        self.time_studied = time_studied
        self.subject = subject
