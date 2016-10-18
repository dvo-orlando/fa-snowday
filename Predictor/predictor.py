#import data
import json
from pprint import pprint

with open('samplejson_hourly.json') as data_file:
    data = json.load(data_file)


#prints data
    #pprint(data)


#Example for accessing the hour of the first "hourly_forecast" object array,
print(data["hourly_forecast"][0]["FCTTIME"]["hour"])
