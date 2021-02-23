#We hard coded the indexes corresponding to the TMIN and TMAX
#columns. Use the header row to determine the indexes for these values, so your program can work
#for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
#for your graph as well.

create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

import csv
from datetime import datetime

open_file = "sitka_weather_2018_simple.csv"
open_file = "death_valley_2018_simple.csv"
place_name = ""
with open(open_file) as c:
    csv_file = csv.reader(c)
    header_row = next(csv_file)

    print(header_row)
    high_pos = header_row.index("TMAX")
    low_pos = header_row.index("TMIN")
    date_pos = header_row.index("DATE")
    name_pos = header_row.index("NAME")

    highs = []
    lows = []
    dates = []

    for row in csv_file:
        try:
            high = int(row[high_pos])
            low = int(row[low_pos])
            converted_date = datetime.strptime(row[date_pos], "%Y-%m-%d")
            place_name = row[name_pos]
        except ValueError:
            print(f"missing data for {converted_date}")
        else:
            highs.append(int(row[high_pos]))
            lows.append(int(row[low_pos]))
            dates.append(converted_date)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)
plt.title(f"Daily high and low temperatures - 2018 {place_name}", fontsize=16)

ax[0].plot(dates, highs, c="red")
ax[0].plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax[1].plot(dates, highs, c="red")
ax[1].plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis="both", labelsize=12)

plt.show()