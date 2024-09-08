# question 1 task 1
import random

moods = ["happy", "sad", "energetic", "calm", "angry", "content"]

days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for day in range(len(days_of_the_week)):
    todays_mood = random.choice(moods)
    print("I feel " + todays_mood + " on " + days_of_the_week[day])
