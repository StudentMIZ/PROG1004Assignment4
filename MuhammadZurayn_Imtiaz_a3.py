'''MuhammadZurayn_Imtiaz_A2.py
created by Muhammad Zurayn Imtiaz
Feb 22, 2022'''

'''Problem: Application Description
Write a program based on the Object Oriented (OO) paradigm that displays the sensors’/sensor’s
data/information for each Sheridan’s building. This information (or data) includes the sensor’s 2-
D position, the different CO2 levels in PPM, and the average reading(s) for one or more
readings. The application will ask for the following: 1) the number of buildings that needs to be
monitored in terms of the CO2 levels in PPM, 2) the building name, and 3) the number of
sensors in each building. Afterwards, for each building, the program will ask for the following:
1) the number of monitored days, and 2) the CO2 reading(s) (PPM) for each day. '''

import statistics
from random import randint

def countdown(end):                                                     # defines and declares function 'countdown', which is used to create a list of integer values up to the number the user inputted when asked
    i = 1                                                               # sets the counter to 1, don't want to include 0 in the list as there is no 'Sensor 0'
    slist = []                                                          # creates an empty list, 'slist', in which values will later be added
    while i <= end:                                                     # this makes the function loop to this point until the last integer value in the list is equal to the number that was inputted
        slist.append(i)                                                 # adds the integer values to the empty list
        i +=1                                                           # increments the counter 'i' by 1 for every loop, until i is <= to the integer the user inputted
    return(slist)

class SheridanSystem:
    def __init__(self, noOfBuild):
        self._noOfBuild = noOfBuild

    def getnoOfBuild(self):
        return self._noOfBuild

    def setnoOfBuild(self, newnoOfBuild):
        self._noOfBuild = newnoOfBuild

    def run(self, noOfBuild):
        while True:                                                         # makes it so the function loops or doesn't as long as certain conditions are met
            try:
                noOfBuild = int(input("Enter the number of buildings: "))         # asks the user to input an integer value, of how many sensors are deployed in the area
                if(noOfBuild < 1):                                                                              # this is to ensure the user can't input anything lower than a value of 1
                    print("Invalid Entry")                                                                          # works to print out a statement letting the user know that they have made an incorrect input
                    print("Re-Enter the number of buildings: ")
                    continue                                                                                        # this makes it so that it loops back to the earlier line of code
            except ValueError:                                                                                      # this is for instances where the user doesn't input the value as an integer, as that is not an accepted entry
                print("Invalid Entry")
                print("Re-Enter the number of buildings: ")
                continue
            else:
                break                                                       # stops the loop as an accepted value was made by the user
        print()                                                             # prints an empty line of code, giving the output a better look for the user (refer to this explanation when used again later)
        building_list = countdown(noOfBuild)                              # creates a new variable that is a list of integers made when the derived value of 'sensors_input' is run through the 'countdown' function
        return building_list
        


class Building:
    def __init__(self, noOfSensors, listOfSensors, buildName):
        self._noOfSensors = noOfSensors
        self._listOfSensors = listOfSensors
        self._buildName = buildName

    def getnoOfSensors(self):
        return self._noOfSensors

    def setnoOfSensors(self, newnoOfSensors):
        self._noOfSensors = newnoOfSensors

    def getlistOfSensors(self):
        return self._listOfSensors

    def setlistOfSensors(self, newlistOfSensors):
        self._listOfSensors = newlistOfSensors

    def getbuildName(self):
        return self._buildName

    def setbuildName(self, newbuildName):
        self._buildName = newbuildName

class Application:
    def __init__(self):
        pass
    def start(self):
        SheridanSystem()

class IotSensors:
    def __init__(self, posX, posY, noDays, avgRead):
        self._posX = posX
        self._posY = posY
        self._noDays = noDays
        self._avgRead = avgRead

    def getposX(self):
        return self._posX

    def setposX(self, newposX):
        self._posX = newposX

    def getposY(self):
        return self._posY

    def setposY(self, newposY):
        self._posY = newposY

    def getnoDays(self):
        return self._noDays

    def setnoDays(self, newnoDays):
        self._noDays = newnoDays

    def getavgRead(self):
        return self._avgRead

    def setavgRead(self, newavgRead):
        self._avgRead = newavgRead

    def sensorPos(self):
        pass

    def sensorReadings(self):
        pass

    def computeAvg(self):
        pass

    

class Co2Sensors:
    def __init__(self, co2Levels):
        self._co2Levels = co2Levels

    def getco2Levels(self):
        return self._co2Levels

    def setco2Levels(self, newco2Levels):
        self._co2Levels = newco2Levels



