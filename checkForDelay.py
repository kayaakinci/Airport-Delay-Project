
null = 'null'


def checkForDelay(airportDict):
    flights = 0
    flightsDelayed = 0
    for flight in airportDict:
        flights += 1
        if flight['codeshared'] == None:
            #gets rid of repeats
            departureStats = flight['departure']
            if departureStats["delay"] != null:
                if departureStats["delay"] != None:
                    if int(departureStats["delay"]) > 6 and int(departureStats["delay"]) % 10 != 0:
                        #gets rid of miscelanious flight delay calls
                        if int(departureStats["delay"])< 20 or int(departureStats["delay"])>29:
                            #gets rid of cargo/mail flight delays
                            flightsDelayed += 1
    return flightsDelayed/flights






