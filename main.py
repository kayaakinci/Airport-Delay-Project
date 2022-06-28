from operator import index
import requests
import json
from getData import *
from airportsDict import *
from checkForDelay import *
from currTime import *
from finalRankings import *
from calculateProbability import * 






finalDictFlightsRatio = {}



def findDelay():
    for airport in airportsDict:
        if airport not in finalDictFlightsRatio:
            print("Calculating Delay Time for:", airport)
            #gets the delayed data of each airport and adds it to the final dictionary
            iataCode = airportsDict[airport]
            flightData = getFlightData(iataCode)
            delayResultFlights = checkForDelay(flightData)
            if delayResultFlights != 0:
                finalDictFlightsRatio[airport] = delayResultFlights + finalDictFlightsRatio.get(airport, 0)







def optionScreen():
    #more options screen
    option1 = input("""Press '1' if you would like to see the delay time for a specific airport. Press '2' if you would like to see the airport catalog. Press '3' if you would like to add an airport to the airport catalog:""")
    if option1 == '1':
        #if the user would like to see the delay time for a specific airport 
        for airport in airportsDict:
            print(airport)
        airportOption = input("Print name of the airport you would like to see the delay of:")
        if airportOption in finalDictFlightsRatio:
            print("---------------------------------")
            print(f"Delay Time for {airportOption} is {finalDictFlightsRatio[airportOption]}")
        else:
            print("---------------------------------")
            print(airportOption, 'is not an option')
    elif option1 =='2':
        for airport in airportsDict:
            print(airport)
    elif option1 == '3':
        addedAirportName = input("Write the name of the airport: ")
        addedAirportIATA = input("Write the IATA code of the airport: ")
        airportsDict[addedAirportName] = addedAirportIATA
        findDelay()
        print("----------------------------------")
        print("Current Day and Time: ", dt_string)
        print("---------------------------------")
        finalRankings(finalDictFlightsRatio)
    print("---------------------------------")
    optionScreen()



    
#Terminal


findDelay()
print("----------------------------------")
print("Current Day and Time: ", dt_string)
print("---------------------------------")
print("The top 3 airports with the highest ratio of delayed flights / total flights")
finalRankings(finalDictFlightsRatio)

print('---------------------------------')

quantityOutput = input("How many airports will you be departing from today? ")
calculateProbabilityOfDelay(quantityOutput, finalDictFlightsRatio)
print('-------------------')
optionInput = input("Press 'o' if you would like to discover more options:  ")
if optionInput == 'o':
    optionScreen()



 




