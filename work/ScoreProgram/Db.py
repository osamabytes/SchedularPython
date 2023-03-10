from pyodbc import connect
from models.Score import Score

class SQL:
    def __init__(self):
        file_path = r"DBQ=C:\Users\osama\OneDrive\Documents\GitHub\SchedularPython\work\ScoreProgram\Schedular.accdb;"
        self.connection = connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' + file_path
        )
        self.cursor = self.connection.cursor()
    def All(self):
        self.cursor.execute('SELECT * FROM Scores')
        rows = self.cursor.fetchall()
        return rows
    def Insert(self, score: Score):
        sql_query = f"INSERT INTO Scores (Habit, Score, DateRecord) VALUES ('{score.habit}', {score.score}, '{score.datetime}')"
        self.cursor.execute(sql_query)
        self.connection.commit()
<<<<<<< HEAD
    def RemoveAll(self):
=======
    def Delete(self):
>>>>>>> 1f08cf6e6d45d1335467d05c188db9f713e4d57e
        sql_query = "DELETE FROM Scores"
        self.cursor.execute(sql_query)
        self.connection.commit()
    def Close(self):
        self.cursor.close()
        self.connection.close()