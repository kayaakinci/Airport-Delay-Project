def finalRankings(finalDict):
    #returns the order of the most delayed airports
    mostDelayedAirportTimes = [0,0,0]
    mostDelayedAirports = [None,None,None]
    for airport in finalDict:
        currTime = finalDict[airport]
        if currTime >= mostDelayedAirportTimes[0] >=mostDelayedAirportTimes[1]:
            #if the current time is the greatest
            mostDelayedAirportTimes[1], mostDelayedAirportTimes[2] = mostDelayedAirportTimes[0], mostDelayedAirportTimes[1]
            mostDelayedAirports[1],mostDelayedAirports[2] = mostDelayedAirports[0], mostDelayedAirports[1]
            mostDelayedAirportTimes[0] = currTime
            mostDelayedAirports[0] = airport
        elif mostDelayedAirportTimes[0]>= currTime >=mostDelayedAirportTimes[1]:
            #if the current time is the 2nd greatest time
            mostDelayedAirportTimes[2] = mostDelayedAirportTimes[1]
            mostDelayedAirports[2] = mostDelayedAirports[1]
            mostDelayedAirportTimes[1] = currTime
            mostDelayedAirports[1] = airport
        elif mostDelayedAirportTimes[0] >= mostDelayedAirportTimes[1] >= currTime >= mostDelayedAirportTimes[2]:
            mostDelayedAirportTimes[2],mostDelayedAirports[2]= currTime,airport
    print('1.', mostDelayedAirports[0],'delay time:',mostDelayedAirportTimes[0])
    print('2.', mostDelayedAirports[1],'delay time:',mostDelayedAirportTimes[1])
    print('3.', mostDelayedAirports[2],'delay time:',mostDelayedAirportTimes[2])
    







