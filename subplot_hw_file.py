# We hard coded the indexes corresponding to the TMIN and TMAX
# columns. Use the header row to determine the indexes for these values, so your program can work
# for Sitka or Death Valley. Use the station name to automatically generate an appropriate title
# for your graph as well.

# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

import csv
from datetime import datetime

# setting up automatic indexing for sitka file
open_sk_file = "sitka_weather_2018_simple.csv"

sk_place_name = ""
with open(open_sk_file) as c:
    csv_file = csv.reader(c)
    header_row = next(csv_file)

    print(header_row)
    high_pos = header_row.index("TMAX")
    low_pos = header_row.index("TMIN")
    date_pos = header_row.index("DATE")
    name_pos = header_row.index("NAME")

    sk_highs = []
    sk_lows = []
    sk_dates = []

    for row in csv_file:
        try:
            high = int(row[high_pos])
            low = int(row[low_pos])
            converted_date = datetime.strptime(row[date_pos], "%Y-%m-%d")
            sk_place_name = row[name_pos]
        except ValueError:
            print(f"missing data for {converted_date}")
        else:
            sk_highs.append(int(row[high_pos]))
            sk_lows.append(int(row[low_pos]))
            sk_dates.append(converted_date)

# setting up automatic indexing for death valley file
open_dv_file = "death_valley_2018_simple.csv"
dv_place_name = ""
with open(open_dv_file) as c:
    csv_file = csv.reader(c)
    header_row = next(csv_file)

    print(header_row)
    high_pos = header_row.index("TMAX")
    low_pos = header_row.index("TMIN")
    date_pos = header_row.index("DATE")
    name_pos = header_row.index("NAME")

    dv_highs = []
    dv_lows = []
    dv_dates = []

    for row in csv_file:
        try:
            high = int(row[high_pos])
            low = int(row[low_pos])
            converted_date = datetime.strptime(row[date_pos], "%Y-%m-%d")
            dv_place_name = row[name_pos]
        except ValueError:
            print(f"missing data for {converted_date}")
        else:
            dv_highs.append(int(row[high_pos]))
            dv_lows.append(int(row[low_pos]))
            dv_dates.append(converted_date)


# creating plot design
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)
plt.suptitle(
    f"Temperature comparison between {sk_place_name} and {dv_place_name}", fontsize=16
)

ax[0].plot(sk_dates, sk_highs, c="red")
ax[0].plot(sk_dates, sk_lows, c="blue")
ax[0].title.set_text(f"{sk_place_name}")
ax[0].fill_between(sk_dates, sk_highs, sk_lows, facecolor="blue", alpha=0.1)

ax[1].plot(dv_dates, dv_highs, c="red")
ax[1].plot(dv_dates, dv_lows, c="blue")
ax[1].title.set_text(f"{dv_place_name}")
ax[1].fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=0.1)

plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.tick_params(axis="both", labelsize=12)

plt.show()