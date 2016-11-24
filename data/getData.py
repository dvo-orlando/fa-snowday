import time
from datetime import datetime
import csv
import wget
import os.path

with open('data/dataset.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:

        #Extract date from row and add 3:00am
        date = row[0] + " 3:00AM"
        dayType = row[1]

        #Create datetime object from each date
        dt = datetime.strptime(date, '%b %d, %Y %I:%M%p')
        #format for url
        dateurl = dt.isoformat('T')

        url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806," + dateurl + "?exclude=currently,minutely,alerts,flags"


        path = "data/raw/" + dt.strftime('%Y-%m-%d') + "." + row[1]

        if not os.path.exists(path):
                filename = wget.download(url, out=path)
