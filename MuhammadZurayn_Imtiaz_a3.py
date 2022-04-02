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

buildName_list = ["A-Building", "B-Building", "C-Building", "D-Building", "E-Building", "F-Building", "G-Building", "H-Building", "I-Building", "J-Building", "K-Building", "L-Building", "M-Building", "N-Building", "O-Building",  "P-Building", "Q-Building", "R-Building", "S-Building", "T-Building", "U-Building", "V-Building", "W-Building", "X-Building", "Y-Building", "Z-Building"]

def countdown(end):                                                                                             # defines and declares function 'countdown', which is used to create a list of integer values up to the number the user inputted when asked
    i = 1                                                                                                       # sets the counter to 1, don't want to include 0 in the list as there is no 'Sensor 0'
    slist = []                                                                                                  # creates an empty list, 'slist', in which values will later be added
    while i <= end:                                                                                             # this makes the function loop to this point until the last integer value in the list is equal to the number that was inputted
        slist.append(i)                                                                                         # adds the integer values to the empty list
        i +=1                                                                                                   # increments the counter 'i' by 1 for every loop, until i is <= to the integer the user inputted
    return(slist)




class SheridanSystem:                                                                                           # class made for the number of buildings, and the names of the buildings
    def __init__(self):
        self._noOfBuild = 0                                                                                     # attributes included

    def getnoOfBuild(self):                                                                                     # accessor method
        return self._noOfBuild

    def setnoOfBuild(self, newnoOfBuild):                                                                       # mutator method
        self._noOfBuild = newnoOfBuild




    def run(self):
        while True:                                                                                             # makes it so the function loops or doesn't as long as certain conditions are met
            try:
                noOfBuild = int(input("Enter the number of buildings: "))                                       # asks the user to input an integer value, of how many sensors are deployed in the area
                if(noOfBuild < 1):                                                                              # this is to ensure the user can't input anything lower than a value of 1
                    print("Invalid Entry")                                                                      # works to print out a statement letting the user know that they have made an incorrect input
                    print("Re-Enter the number of buildings: ")
                    continue                                                                                    # this makes it so that it loops back to the earlier line of code
            except ValueError:                                                                                  # this is for instances where the user doesn't input the value as an integer, as that is not an accepted entry
                print("Invalid Entry")
                print("Re-Enter the number of buildings: ")
                continue
            else:
                break                                                                                           # stops the loop as an accepted value was made by the user
        print()                                                                                                 # prints an empty line of code, giving the output a better look for the user (refer to this explanation when used again later)
        building_list = countdown(noOfBuild)                                                                    # creates a new variable that is a list of integers made when the derived value of 'sensors_input' is run through the 'countdown' function
        buildNameList = []
        for _ in  building_list:
            print("Building", _)           
            while True:
                try:
                    b_input = print(input("Enter the building name: "))
                    if(b_input in buildName_list):                                                              # checks if the value of the variable is above 50, or below 20, as that is the given range in the problem
                        print(b_input)                                                                          # lets the user know that the input isn't accepted, and they must try again
                        buildNameList.append(b_input)
                        obj2 = Building(buildNameList)
                        for _ in buildNameList:
                            obj2.createSensors()
                            break                         
                except ValueError:                                                                              # doesn't accept any other type of value other than of the int class
                    print()
                    print("Invalid Entry")                                                                      # informs the user that the value is not accepted and to try again
                    print("Re-Enter the building name: ")
                    print()
                    continue                                                                                    # loops back to ask the user to input a value again
                else:
                    print()
                    print("Invalid Entry")                                                                      # lets the user know that the input isn't accepted, and they must try again
                    print("Re-Enter the building name: ")
                    print()
                    continue
        



class Building:
    def __init__(self, buildName):
        self._noOfSensors = 4
        self._listOfSensors = []
        self._buildName = buildName

    def getnoOfSensors(self):                                                                                       # accessor method                             
        return self._noOfSensors

    def setnoOfSensors(self, newnoOfSensors):                                                                       # mutator method
        self._noOfSensors = newnoOfSensors

    def getlistOfSensors(self):                                                                                     # accessor method
        return self._listOfSensors

    def setlistOfSensors(self, newlistOfSensors):                                                                   # mutator method
        self._listOfSensors = newlistOfSensors

    def getbuildName(self):                                                                                         # accessor method
        return self._buildName

    def setbuildName(self, newbuildName):                                                                           # mutator
        self._buildName = newbuildName

    def createSensors(self):
        while True:                                                                                                 # makes it so the function loops or doesn't as long as certain conditions are met
            try:
                noOfSensors = int(input("Enter the number of sensors deployed across Sheridan Campus: "))           # asks the user to input an integer value, of how many sensors are deployed in the area
                if(noOfSensors < 1):                                                                                # this is to ensure the user can't input anything lower than a value of 1
                    print("Invalid Entry")                                                                          # works to print out a statement letting the user know that they have made an incorrect input
                    continue                                                                                        # this makes it so that it loops back to the earlier line of code
            except ValueError:                                                                                      # this is for instances where the user doesn't input the value as an integer, as that is not an accepted entry
                print("Invalid Entry")
                continue
            else:
                break                                                                                                 # stops the loop as an accepted value was made by the user
        print()
        listOfSensors = countdown(noOfSensors)                                                                        # creates a new variable that is a list of integers made when the derived value of 'noOfSensors' is run through the 'countdown' function
        for _ in listOfSensors:                                                                                       # for loop is used, with the definite amount of times it will loop being how many values there are in the sensor_list
            print("Sensor", _)                                                                                        # prints out which sensor the following question will be about, as well as the random position of the sensor
            noDays = 0
            while True:
                try:
                    noDays = int(input("Enter the number of days for the readings: "))                                # asks the user to input the number of days for each sensor
                    if(noDays < 1):                                                                                   # makes it so user can't input less than 1, since we only care to measure CO2 if the sensor has been put to use across at least one day
                        print("Incorrect Entry! Please try again.")                                                   # again informs the user that they have made an unaccepted input and to try again
                        continue                                                                                      # loops back until the user doesn't make the same error
                except ValueError:                                                                                    # won't accept an input that is not an int class
                    print("Incorrect Entry! Please try again.")                                                       # again informs the user that they have made an unaccepted input and to try again
                    continue
                else:
                    break                                                                                             # while loop is not run again as it doesn't match the above conditions, meaning it is accepted
            days_list = countdown(noDays)
            for _ in days_list:
                obj3 = Co2Sensors()
                obj3.carbon_values()
        

    def printSenInfo(self, buildName, posX, posY, ):                                                                  # prints out all of the info, including the building name, its position, the daily Co2 readings, and as well as the average value of the Co2 readings
            print("This is for building: ", buildName)
            print(("x: ", posX, "y: ", posY))

            




class Application:
    def __init__(self):
        pass

    def start(self):                                                                                                    # start method that stars the Sheridan System
        test = SheridanSystem()
        test.run()




class IotSensors():
    def __init__(self):
        self._posX = (0.1, 0.1)
        self._posY = (0.1, 0.1)
        self._noDays = 0
        self._avgRead = 0.1

    def getposX(self):                                                                                                  # accessor method
        return self._posX

    def setposX(self, newposX):                                                                                         # mutator method
        self._posX = newposX

    def getposY(self):                                                                                                  # accessor method
        return self._posY

    def setposY(self, newposY):                                                                                         # mutator method
        self._posY = newposY

    def getnoDays(self):                                                                                                # accessor method
        return self._noDays

    def setnoDays(self, newnoDays):                                                                                     # mutator method
        self._noDays = newnoDays

    def getavgRead(self):                                                                                               # accessor method
        return self._avgRead

    def setavgRead(self, newavgRead):                                                                                   # mutator method
        self._avgRead = newavgRead

    def sensorPos(self):
        pass

    def sensorReadings(self):
        pass

    def computeAvg(self):
        pass

    



class Co2Sensors(IotSensors):
    carbon_values = []
    def __init__(self):
        self._co2Levels = 0

    def getco2Levels(self):                                                                                             # accessor method
        return self._co2Levels

    def setco2Levels(self, newco2Levels):                                                                               # mutator method
        self._co2Levels = newco2Levels

    def sensorPos(self):
        posX = randint(0,100)
        posY = randint (0,100)
        return (posX, posY)

    def sensorReadings(self):
        carbon_values = []
        print(input("Enter the CO2 Reading (PPM) for Day", _, ":"))                                                     # lets the user know which day's CO2 value they should input
        while True:
            try:
                co2Levels = int(input())                                                                                # asks the user to input a variable under the int class, which will be put into the 'carbon_values' list
                if(co2Levels < 0):                                                                                      # checks if the value of the variable is above 50, or below 20, as that is the given range in the problem
                    print("Invalid Entry")                                                                              # lets the user know that the input isn't accepted, and they must try again
                    continue                                                                                            # loops back to the if statement
            except ValueError:                                                                                          # doesn't accept any other type of value other than of the int class
                print("Invalid Entry")                                                                                  # informs the user that the value is not accepted and to try again
                continue                                                                                                # loops back to ask the user to input a value again
            else:
                break                                                                                                   # ends the loop as an accepted value is given
        carbon_values.append(co2Levels)
        computeAvg()

        def computeAvg():
            avgRead = round(statistics.mean(carbon_values), 2)                                                          # averages out all the values given by the user, while also rounding the values to 2 decimal points
            print("Rounded Average Readings", avgRead, "PPM")                                                           # prints out the value derived from 'avgRead' in the output of the code, for the user to see
            print()
            carbon_values.clear()




obj1 = Application()
obj1.start()
obj3 = Building
