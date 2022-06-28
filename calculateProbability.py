#calculates the probability of a delay for a passenger given the route

def calculateProbabilityOfDelay(quantityOutput, finalDictFlightsRatio):
    probability = 1
    listOfProbs = []
    for i in range(int(quantityOutput)):
        airportDestination = input(f'name of #{i+1} airport:')
        if airportDestination not in finalDictFlightsRatio:
            print("Not an airport in catalog-----")
            airportDestination = input(f'name of #{i+1} airport:')
        else:
            probability *= finalDictFlightsRatio[airportDestination]
            listOfProbs.append(finalDictFlightsRatio[airportDestination])
    print('                       ')
    print('                        ')
    print(f"There is a {probability} chance that all of your flights get delayed")
    if len(listOfProbs) > 1:
        print(f"There is a {min(listOfProbs)}  - {max(listOfProbs)} chance that one of your flights get delayed.")