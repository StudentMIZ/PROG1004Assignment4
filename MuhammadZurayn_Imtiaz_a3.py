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


class SheridanSystem:
    def __init__(self, noOfBuild):
        self._noOfBuild = noOfBuild

    def getA(self):
        return self._noOfBuild

    def setA(self, newnoOfBuild):
        self._noOfBuild = newnoOfBuild


class Building:
    def __init__(self, noOfSensors, listOfSensors, buildName):
        self._noOfSensors = noOfSensors
        self._listOfSensors = listOfSensors
        self._buildName = buildName

    def getA(self):
        return self._noOfSensors

    def setA(self, newnoOfSensors):
        self._noOfSensors = newnoOfSensors

    def getB(self):
        return self._listOfSensors

    def setB(self, newlistOfSensors):
        self._listOfSensors = newlistOfSensors

    def getC(self):
        return self._buildName

    def setC(self, newbuildName):
        self._buildName = newbuildName

class Application:
    def __init__(self):
        pass

class IotSensors:
    def __init__(self, posX, posY, noDays, avgRead):
        self._posX = posX
        self._posY = posY
        self._noDays = noDays
        self._avgRead = avgRead

    def get1(self):
        return self._posX

    def set1(self, newposX):
        self._posX = newposX

    def get2(self):
        return self._posY

    def set2(self, newposY):
        self._posY = newposY

    def get3(self):
        return self._noDays

    def set3(self, newnoDays):
        self._noDays = newnoDays

    def get4(self):
        return self._avgRead

    def set4(self, newavgRead):
        self._avgRead = newavgRead

    

class Co2Sensors:
    def __init__(self, co2Levels):
        self._co2Levels = co2Levels

    def getV1(self):
        return self._co2Levels

    def setV1(self, newco2Levels):
        self._co2Levels = newco2Levels



