print("\n********************************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a function randomly chosing the weather from a list
def weather():
    weatherForecast = ["Sunny","Snowing","Blizzard","Foggy","Windy","Icy","Rain","Cloudy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition
