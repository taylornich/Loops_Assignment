# question 2 task 1

import random

moods = ["happy", "sad", "energetic", "calm", "angry", "content"]

days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

time_of_day = ["morning", "afternoon", "evening"]

for day in range(len(days_of_the_week)):
    for time in range(len(time_of_day)):
        current_mood = random.choice(moods)
        print("During the " + time_of_day[time] + " on " + days_of_the_week[day] + " I was feeling " + current_mood)
        