#Task 1: Your Mood Tracker
import random
moods = ("Happy", "Sad", "Energetic", "Calm")
time_of_day = "morning", "afternoon", "evening"
days_of_the_week = ["monday", "tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for index in range(len(time_of_day)):
     print("On " + time_of_day[index] + " you were " + random.choice(moods))
for index in range(len(days_of_the_week)):
     print(("On " + days_of_the_week[index]+ " you were " + random.choice(moods)))

