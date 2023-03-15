class Score:
    def __init__(self, startDateTime, endDateTime, habit, score):
        self.startDateTime = startDateTime
        self.endDateTime = endDateTime
        self.habit = habit
        self.score = score
    
    def set_startDateTime(self, startDateTime):
        self.startDateTime = startDateTime
    def get_startDateTime(self):
        return self.startDateTime
    
    def set_endDateTime(self, endDateTime):
        self.endDateTime = endDateTime
    def get_endDateTime(self):
        return self.endDateTime
    
    def set_habit(self, habit):
        self.habit = habit
    def get_habit(self):
        return self.habit
    
    def set_score(self, score):
        self.score = score
    def get_score(self):
        return self.score
    
