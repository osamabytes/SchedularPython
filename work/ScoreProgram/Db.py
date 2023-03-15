from pyodbc import connect
from models.Score import Score
from models.Mark import Mark

connectionStr = r"C:\Users\osama\Documents\Github\SchedularPython\work\ScoreProgram\Schedular.accdb;"

class ScoreSQL:
    def __init__(self):
        file_path = r"DBQ=" + connectionStr
        self.connection = connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' + file_path
        )
        self.cursor = self.connection.cursor()
    def All(self):
        self.cursor.execute('SELECT * FROM Scores')
        rows = self.cursor.fetchall()
        return rows
    def Insert(self, score: Score):
        sql_query = f"INSERT INTO Scores (StartDate, EndDate, Habit, Score) VALUES ('{score.startDateTime}', '{score.endDateTime}', '{score.habit}', {score.score})"
        self.cursor.execute(sql_query)
        self.connection.commit()
    def RemoveAll(self):
        sql_query = "DELETE FROM Scores"
        self.cursor.execute(sql_query)
        self.connection.commit()
    def Close(self):
        self.cursor.close()
        self.connection.close()

class MarkSQL:
    def __init__(self):
        file_path = r"DBQ=" + connectionStr
        self.connection = connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' + file_path
        )
        self.cursor = self.connection.cursor()
    def All(self):
        self.cursor.execute('SELECT * FROM Marks')
        rows = self.cursor.fetchall()
        return rows
    def Insert(self, mark: Mark):
        sql_query = f"INSERT INTO Marks(Score, Habit, DateRecorded, DayRecorded) VALUES ({mark.score}, '{mark.habit}', '{mark.date_recorded}', '{mark.day_recorded}')"
        self.cursor.execute(sql_query)
        self.connection.commit()
    def RemoveAll(self):
        sql_query = "DELETE FROM Marks"
        self.cursor.execute(sql_query)
        self.connection.commit()
    def Close(self):
        self.cursor.close()
        self.connection.close()