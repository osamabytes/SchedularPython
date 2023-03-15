from models.Score import Score
from Db import ScoreSQL
from datetime import datetime

days = []
scores = []
final_scores = dict()
days_in_week = 7
#Start Function
def ReadScore():
    data_list = []
    with open('Days_Score.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            data_list.append(line.strip())
        return data_list
def CalculateFinalScores(score_list):
    for score in score_list:
        scr_data = score.split(":")
        work = scr_data[0]
        scr = scr_data[1]
        if work in final_scores:
            final_scores[work] += float(scr)
        else:
            final_scores[work] = float(scr)
#End Function

days_scores = ReadScore()
#iterate through each day scores and append to scores
for score_data in days_scores:
    data_parts = score_data.split("-")
    day_name = data_parts[0]
    days.append(day_name)
    data = data_parts[1][1:-1]
    scores.append(data.split(","))

for score in scores:
    CalculateFinalScores(score)

for key, value in final_scores.items():
    final_scores[key] = round(value / days_in_week, 2)

# Record the Scores in DB
sql = ScoreSQL()
# input for the date
start_date = input("Enter Start Date by Year - Month - Date: ")
end_date = input("Enter End Date by Year - Month - Date: ")
# split start and end date
start_datetime_arr = start_date.split(" ")
end_datetime_arr = end_date.split(" ")
for key, value in final_scores.items():
    sql.Insert(Score(
            datetime(int(start_datetime_arr[0]), int(start_datetime_arr[1]), int(start_datetime_arr[2])), 
            datetime(int(end_datetime_arr[0]), int(end_datetime_arr[1]), int(end_datetime_arr[2])), 
            key, value)
        )
sql.Close()