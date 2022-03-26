import statistics
from random import randint

def countdown(end):                                                     # defines and declares function 'countdown', which is used to create a list of integer values up to the number the user inputted when asked
    i = 1                                                               # sets the counter to 1, don't want to include 0 in the list as there is no 'Sensor 0'
    slist = []                                                          # creates an empty list, 'slist', in which values will later be added
    while i <= end:                                                     # this makes the function loop to this point until the last integer value in the list is equal to the number that was inputted
        slist.append(i)                                                 # adds the integer values to the empty list
        i +=1                                                           # increments the counter 'i' by 1 for every loop, until i is <= to the integer the user inputted
    return(slist)


def start():
    pass

def run():
    while True:                                                         # makes it so the function loops or doesn't as long as certain conditions are met
        try:
            building_input = int(input("Enter the number of buildings: "))         # asks the user to input an integer value, of how many sensors are deployed in the area
            if(building_input < 1):                                                                              # this is to ensure the user can't input anything lower than a value of 1
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
    building_list = countdown(building_input)                              # creates a new variable that is a list of integers made when the derived value of 'sensors_input' is run through the 'countdown' function
    return building_list
building_list = run()
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

def createSensors():
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
    return sensor_list 

def printSenInfo():
    pass

def sensorPos():
    posX = randint(0,100)
    posY= randint (0,100)

carbon_values = []
def sensorReadings(): 
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

def computeAVG():
    c_values = round(statistics.mean(carbon_values), 2)         # averages out all the values given by the user, while also rounding the values to 2 decimal points
    print("Rounded Average Readings", c_values, "PPM")              # prints out the value derived from 'c_values' in the output of the code, for the user to see
    print()
    carbon_values.clear()
    
