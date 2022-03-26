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
    return(slist)                                                       # returns the value, so when the function 'countdown' is called, the value is given

def sensor_data():                                                      # defines and declares the function 'sensor_data' which asks the user for how many sensors would there be, ultimately creating a list of sensors depending on the user's input
    while True:                                                         # makes it so the function loops or doesn't as long as certain conditions are met
        try:
            sensors_input = int(input("Enter the number of sensors deployed across Sheridan Campus: "))         # asks the user to input an integer value, of how many sensors are deployed in the area
            if(sensors_input < 1):                                                                              # this is to ensure the user can't input anything lower than a value of 1
                print("Invalid Entry")                                                                          # works to print out a statement letting the user know that they have made an incorrect input
                continue                                                                                        # this makes it so that it loops back to the earlier line of code
        except ValueError:                                                                                      # this is for instances where the user doesn't input the value as an integer, as that is not an accepted entry
            print("Invalid Entry")
            continue
        else:
            break                                                       # stops the loop as an accepted value was made by the user
    print()                                                             # prints an empty line of code, giving the output a better look for the user (refer to this explanation when used again later)
    sensor_list = countdown(sensors_input)                              # creates a new variable that is a list of integers made when the derived value of 'sensors_input' is run through the 'countdown' function
    return sensor_list                                                  # returns the value, so when the function 'sensor_data' is called, the value is given

carbon_values = []                                                      # creates a variable that is an empty list, which will be filled with values of carbon values for later


def sensor_function():                                                  # defines and declares the funtion 'sensor_function' which asks the user to input the number of days measured for each sensor, as well as the values of CO2 levels for each day. It then averages those values out for each sensor.
    sensor_list = sensor_data()                                         # calls the variable from the function 'sensor_data
    for _ in sensor_list:                                               # for loop is used, with the definite amount of times it will loop being how many values there are in the sensor_list
        sensor_x = randint(0,100), randint(0,100)                       # assigns a random position for each sensor in the output, in a 100 x 100 m2 area
        print("This is for Sensor", _, "at position", sensor_x)         # prints out which sensor the following question will be about, as well as the random position of the sensor
        days_input = 0
        while True:
            try:
                days_input = int(input("Enter the number of days for the sensor(s) to collect CO2 levels:"))                            # asks the user to input the number of days for each sensor
                if(days_input < 1):                                                                                                     # makes it so user can't input less than 1, since we only care to measure CO2 if the sensor has been put to use across at least one day
                    print("Invalid Entry")                                                                                              # again informs the user that they have made an unaccepted input and to try again
                    continue                                                                                                            # loops back until the user doesn't make the same error
            except ValueError:                                                                                                          # won't accept an input that is not an int class
                print("Invalid Entry")                                                                                                  # again informs the user that they have made an unaccepted input and to try again
                continue
            else:
                break                                                   # while loop is not run again as it doesn't match the above conditions, meaning it is accepted
        days_list = countdown(days_input)                               # creates a new variable that is a list of integers made when the derived value of 'days_input' is run through the 'countdown' function
        for _ in days_list:                                             # for loop is used, with the definite amount of times it will loop being how many values there are in the days_list
            print("Enter the CO2 Reading (PPM) for Day", _, ":")                      # lets the user know which day's CO2 value they should input
            while True:
                try:
                    carbon_input = int(input())                         # asks the user to input a variable under the int class, which will be put into the 'carbon_values' list
                    if(carbon_input < 0):                               # checks if the value of the variable is above 50, or below 20, as that is the given range in the problem
                        print("Invalid Entry")                          # lets the user know that the input isn't accepted, and they must try again
                        continue                                        # loops back to the if statement
                except ValueError:                                      # doesn't accept any other type of value other than of the int class
                    print("Invalid Entry")                              # informs the user that the value is not accepted and to try again
                    continue                                            # loops back to ask the user to input a value again
                else:
                    break                                               # ends the loop as an accepted value is given
            carbon_values.append(carbon_input)
            c_values = round(statistics.mean(carbon_values), 2)         # averages out all the values given by the user, while also rounding the values to 2 decimal points
        print("Rounded Average Readings", c_values, "PPM")              # prints out the value derived from 'c_values' in the output of the code, for the user to see
        print()
        carbon_values.clear()                                           # clears the list of the values so the list can include values only from each day for each sensor, giving an average only for CO2 across all days measured for each singular sensor

sensor_function()                                                       # runs the function 'sensor_function()'


class SheridanSystem:
    def __init__(self, noOfBuild):
        self._inita = noOfBuild

    def getA(self):
        return self._inita

    def setA(self, newInita):
        self._inita = newInita


class Building:
    def __init__(self, noOfSensors, listOfSensors, buildName):
        self._inita = noOfSensors
        self._initb = listOfSensors
        self._initc = buildName

    def getA(self):
        return self._inita

    def setA(self, newInita):
        self._inita = newInita

    def getB(self):
        return self._initb

    def setB(self, newInitb):
        self._initb = newInitb

    def getC(self):
        return self._initc

    def setC(self, newInitc):
        self._initc = newInitc

class Application:
    def __init__(self):
        pass

class IotSensors:
    def __init__(self, posX, posY, noDays, avgRead):
        self._att1 = posX
        self._att2 = posY
        self._att3 = noDays
        self._att4 = avgRead

    def get1(self):
        return self._att1

    def set1(self, newAtt1):
        self._att1 = newAtt1

    def get2(self):
        return self._att2

    def set2(self, newAtt2):
        self._att2 = newAtt2

    def get3(self):
        return self._att3

    def set3(self, newAtt3):
        self._att3 = newAtt3

    def get4(self):
        return self._att4

    def set4(self, newAtt4):
        self._att4 = newAtt4

    

class Co2Sensors:
    def __init__(self, co2Levels):
        self._var1 = co2Levels

    def getV1(self):
        return self._var1

    def setV1(self, newVar1):
        self._var1 = newVar1



