import time
from datetime import datetime
import csv
import wget

counter=0
with open('snowdays.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:

        #Extract date from row and add 3:00am
        date = row[0] + " 3:00AM"
        dayType = row[1]

        #Create datetime object from each date
        x = datetime.strptime(date, '%b %d, %Y %I:%M%p')

        #format for url
        r = x.isoformat('T')

        url = "https://api.darksky.net/forecast/bd882334266c9cbc88d74adff896684a/44.0165,-70.9806," + r + "?exclude=currently,minutely,hourly,alerts,flags"

        if dayType=="1":
            filename = wget.download(url, out= "raw/" + str(counter) + ".snowday")
        else:
            filename = wget.download(url, out="raw/" + str(counter) + ".day")

        counter=counter+1
