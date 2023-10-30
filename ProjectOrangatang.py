print("***************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Function that List Gas Station, randomly choosing one, and Return its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Function will call the gasLevelGauge to determine gas level and then find a close gas station if low
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    print(milesToGasStationsLow)

gasLevelAlert()