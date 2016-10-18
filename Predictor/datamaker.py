import numpy as np
import json

#features
#temperature
#dewpoint
#windspead
#humidity
#winddirection
#visibility
#pressure
#windchill
#precipitation

#import any historical json to create array of feature values
with open('historical_data/20140106.json') as data_file:
    data = json.load(data_file)
    
print(data['history']['observations'][0]['date']['year'])
