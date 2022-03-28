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
    def __init__(self):
        self._noOfBuild = 0
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
        for _ in  building_list:
            print("Bulding", _)
            print("Enter the building name:")                      # lets the user know which day's CO2 value they should input
        while True:
            try:
                b_input = int(input())                         # asks the user to input a variable under the int class, which will be put into the 'carbon_values' list
                if(b_input < 0):                               # checks if the value of the variable is above 50, or below 20, as that is the given range in the problem
                    print("Invalid Entry")                          # lets the user know that the input isn't accepted, and they must try again
                    print("Re-Enter the building name: ")
                    continue                                        # loops back to the if statement
            except ValueError:                                      # doesn't accept any other type of value other than of the int class
                print("Invalid Entry")                              # informs the user that the value is not accepted and to try again
                print("Re-Enter the building name: ")
                continue                                            # loops back to ask the user to input a value again
            else:
                break
        


class Building:
    def __init__(self):
        self._noOfSensors = 4
        self._listOfSensors = []
        self._buildName = "buildName"

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

    def createSensors(self, noOfSensors, listOfSensors):
        while True:                                                         # makes it so the function loops or doesn't as long as certain conditions are met
            try:
                noOfSensors = int(input("Enter the number of sensors deployed across Sheridan Campus: "))         # asks the user to input an integer value, of how many sensors are deployed in the area
                if(noOfSensors < 1):                                                                              # this is to ensure the user can't input anything lower than a value of 1
                    print("Invalid Entry")                                                                          # works to print out a statement letting the user know that they have made an incorrect input
                    continue                                                                                        # this makes it so that it loops back to the earlier line of code
            except ValueError:                                                                                      # this is for instances where the user doesn't input the value as an integer, as that is not an accepted entry
                print("Invalid Entry")
                continue
            else:
                break                                                       # stops the loop as an accepted value was made by the user
        print()                                                             # prints an empty line of code, giving the output a better look for the user (refer to this explanation when used again later)
        listOfSensors = countdown(noOfSensors)                              # creates a new variable that is a list of integers made when the derived value of 'sensors_input' is run through the 'countdown' function
        return listOfSensors 
        

    def printSenInfo(self, buildName):
        pass

class Application:
    def __init__(self):
        pass
    def start(self):
        SheridanSystem()

class IotSensors:
    def __init__(self):
        self._posX = (0.1, 0.1)
        self._posY = (0.1, 0.1)
        self._noDays = 0
        self._avgRead = 0.1

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
    carbon_values = []
    def __init__(self):
        self._co2Levels = 0

    def getco2Levels(self):
        return self._co2Levels

    def setco2Levels(self, newco2Levels):
        self._co2Levels = newco2Levels

    def sensorPos(self, posX, posY):
        posX = randint(0,100)
        posY = randint (0,100)

    def sensorReadings(self, co2Levels, carbon_values):
        for _ in 
        print("Enter the CO2 Reading (PPM) for Day", _, ":")                      # lets the user know which day's CO2 value they should input
        while True:
            try:
                co2Levels = int(input())                         # asks the user to input a variable under the int class, which will be put into the 'carbon_values' list
                if(co2Levels < 0):                               # checks if the value of the variable is above 50, or below 20, as that is the given range in the problem
                    print("Invalid Entry")                          # lets the user know that the input isn't accepted, and they must try again
                    continue                                        # loops back to the if statement
            except ValueError:                                      # doesn't accept any other type of value other than of the int class
                print("Invalid Entry")                              # informs the user that the value is not accepted and to try again
                continue                                            # loops back to ask the user to input a value again
            else:
                break                                               # ends the loop as an accepted value is given
        carbon_values.append(co2Levels)


    def computeAvg(self, carbon_values):
        c_values = round(statistics.mean(carbon_values), 2)         # averages out all the values given by the user, while also rounding the values to 2 decimal points
        print("Rounded Average Readings", c_values, "PPM")              # prints out the value derived from 'c_values' in the output of the code, for the user to see
        print()
        carbon_values.clear()




