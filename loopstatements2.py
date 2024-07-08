#PythonLoopStatements_Assignment2

import random
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]
for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time}, you were feeling {mood}.")