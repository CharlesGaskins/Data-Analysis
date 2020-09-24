import requests
import pandas as pd
import time
import csv
import os
from datetime import date

# SETTING UP AN EMPTY CSV TO CATCH AND STORE API DATA PULL

filename = "ISS_orbit" + str(date.today()) + ".csv"
with open(filename, 'w'):
    pass
iss_url = "https://api.wheretheiss.at/v1/satellites/25544/"

# FUNCTION THAT WILL FORMAT CORRECTLY ANY JSON INFORMATION AND APPEND TO A BLANK CSV
def dataPull(url):
    response = requests.get(iss_url)
    data = response.json()
    info = list(data.values())
    headers = list(data.keys())
    if os.stat(filename).st_size == 0:
        with open(filename, 'w', ) as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
    else:
        with open(filename, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(info)
    time.sleep(1)
    return filename

# FUNCTION TO ISOLATE THE LAT AND LON OF THE SATELLITE SO WE CAN MAKE SURE THE CORRECT INFORMATION AND AMOUNT IS BEING
# CONSUMED
def coords(csv):
    lon = []
    lat = []
    df = pd.read_csv(filename)
    lon = list(df['longitude'])
    lat = list(df['latitude'])
    longitude = (lon[-100:])
    latitude = (lat[-100:])
    return longitude, latitude

# RUNNING AN INFINITE LOOP SO AS TO PULL REAL TIME DATA AND FEED INTO CSV
while True:
    dataPull(iss_url)
    coords(filename)
    x, y = coords(filename)
    print(x)
    print(len(x))
