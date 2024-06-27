#Task 1: Your Mood Today 
import random
moods = ("Happy", "Sad", "Energetic", "Calm")
days_of_the_week = ("monday", "tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday")

for index in range(len(days_of_the_week)): 
    print("On " + days_of_the_week[index]+ " I am feeling " + random.choice(moods))