from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib.cbook as cbook
import matplotlib.image as image
import matplotlib.dates as mdates
from datetime import date
import datetime
import pandas as pd
import pytz
import time

filename = "../satellite_tracker/Data_intake/ISS_orbit" + str(date.today()) + ".csv"

# READING REAL TIME DATA, TRANSFORMING EPOCH TO DATETIME AND DROPPING ALL EMPTY ROWS
df = pd.read_csv(filename)
ts = []
# lon = list(df['longitude'][-74:])
# lat = list(df['latitude'][-74:])
lon = list(df['longitude'])
lat = list(df['latitude'])
alt = list(df['altitude'])
vel = list(df['velocity'])
epoch = list(df['timestamp'])
visibility = list(df['visibility'])
for i in epoch:
    ts.append(datetime.datetime.fromtimestamp(i).strftime("%I:%M:%S"))

df = df.dropna()
# print(df)
df.to_csv(r"../satellite_tracker/visualization/cleansed_orbit" + str(date.today()) + ".csv")

# ANIMATED LINE GRAPH---ALTITUDE

fig, ax = plt.subplots()
line, = ax.plot(ts, alt, color='k')
fig.autofmt_xdate()


def update(num, x, y, line):
    line.set_data(x[:num], y[:num])

    return line,


ani = animation.FuncAnimation(fig, update, fargs=[ts, alt, line],
                              interval=100, blit=True)
fig.autofmt_xdate()
plt.xticks(rotation=70)
plt.xlabel('1 rotation around Earth')
plt.ylabel('Altitude')
plt.title('How the altitude of the ISS changes as it circles Earth')
plt.show()

# ANIMATED LINE GRAPH---VELOCITY
fig, ax = plt.subplots()
line, = ax.plot(ts, vel, color='k')
fig.autofmt_xdate()


def update(num, x, y, line):
    line.set_data(x[:num], y[:num])

    return line,


ani = animation.FuncAnimation(fig, update, fargs=[ts, vel, line],
                              interval=100, blit=True)
plt.xticks(rotation=70)
plt.xlabel('1 rotation around Earth')
plt.ylabel('Velocity')
plt.title('How the velocity of the ISS changes as it circles Earth')
plt.show()

# ANIMATED GLOBAL PLOTS
plt.figure(figsize=(20, 10))
m = Basemap(width=300000, height=300000, projection='lcc',
            resolution='c', lat_0=51.25, lon_0=-4)

m.drawcoastlines()

m.drawcountries()
m = Basemap(projection='cyl')
m.bluemarble()
date = datetime.datetime.utcnow()
m.nightshade(date)  # VISUAL REPRESENTATION OF WHERE IT IS NIGHT AND DATA ON EARTH
print(len(lon))
for i in range(len(lon)):
    x, y = m(lon[i], lat[i])
    m.scatter(x, y, s=10, c='white', marker='>', zorder=2)

#
plt.show()


def animate(i):
    # THIS WILL NOW DO EVERYTHING WE NEED TO MAKE THE LINE MOVE
    line.set_data(lon[:i], lat[:i])
    return line,


anim = animation.FuncAnimation(fig, animate, interval=10)
