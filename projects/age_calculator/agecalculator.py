from datetime import datetime, timedelta
import math

class AgeCalculator:
    def __init__(self, date, now=datetime.now()):
        self.date = date
        self.now = now
        self.difference = 0

    def set_difference(self):
        date = datetime.strptime(self.date, "%Y-%m-%d")
        difference = self.now - date
        self.difference = difference.days

    def age_seconds(self):
        return ("seconds", self.difference * 24 * 60 * 60)

    def age_minutes(self):
        return ("minutes", self.difference * 24 * 60)

    def age_hours(self):
        return ("hours", self.difference * 24)
    
    def age_days(self):
        return ("days", self.difference)

    def age_weeks(self):
        return ("weeks", math.floor(self.difference / 7))

    def age_months(self):
        return ("months", math.floor(self.difference / 30.5))
    


