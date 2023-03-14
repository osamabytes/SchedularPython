class Mark:
    def __init__(self, habit, score, date_recorded, day_recorded):
        self.habit = habit
        self.score = score
        self.date_recorded = date_recorded
        self.day_recorded = day_recorded
    
    def set_habit(self, habit):
        self.habit = habit
    def get_habit(self):
        return self.habit
    
    def set_score(self, score):
        self.score = score
    def get_score(self):
        return self.score
    
    def set_date_recorded(self, date_recorded):
        self.date_recorded = date_recorded
    def get_date_recorded(self):
        return self.date_recorded
    
    def set_day_recorded(self, day_recorded):
        self.day_recorded = day_recorded
    def get_day_recorded(self):
        return self.day_recorded