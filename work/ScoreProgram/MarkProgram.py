from models.Mark import Mark
from Db import MarkSQL
from datetime import datetime

# Start Function
def ReadScore():
    data_list = []
    with open('work\ScoreProgram\Days_Score.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            data_list.append(line.strip())
    return data_list
# End Function

scores = ReadScore()
score_set = dict()
# Iterate thorugh scores
for score in scores:
    data_parts = score.split("-")
    day = data_parts[0]
    score_set[day] = (data_parts[1][1:-1]).split(",")

sql = MarkSQL()
# Iterate thorugh score set
for day, score in score_set.items():
    scoresData = score
    date_param = input("Enter Date by Year - Month - Date: ")
    dates = date_param.split(" ")
    for data in scoresData:
        s = data.split(":")
        habit = s[0]
        scoreNum = s[1]
        sql.Insert(mark=Mark(habit, float(scoreNum), datetime(int(dates[0]), int(dates[1]), int(dates[2])), day))
sql.Close()