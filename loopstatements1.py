#PythonLoopStatements_Assignment1

import random
moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(len(days_of_week)):
    mood = random.choice(moods)
    print(f"On {days_of_week[i]}, you were feeling {mood}.")