import requests
import json
from accessKey import *

# api from https://aviation-edge.com\




def getFlightData(iataCode):
    api_result = requests.get(f'http://aviation-edge.com/v2/public/timetable?key={accessKey}&iataCode={iataCode}&type=departure')
    api_response = api_result.json() 
    json_file = json.dumps(api_response, indent = 4, sort_keys=True)
    dict_file = json.loads(json_file)
    return dict_file






