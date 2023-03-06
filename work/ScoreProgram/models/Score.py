class Score:
    def __init__(self, datetime, habit, score):
        self.datetime = datetime
        self.habit = habit
        self.score = score
    
    def set_datetime(self, datetime):
        self.datetime = datetime
    def get_datetime(self):
        return self.datetime
    
    def set_habit(self, habit):
        self.habit = habit
    def get_habit(self):
        return self.habit
    
    def set_score(self, score):
        self.score = score
    def get_score(self):
        return self.score
    
