import csv
from datetime import datetime

# sitka file
open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")
header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs_sk = []
lows_sk = []
dates_sk = []

for row in csv_file:
    highs_sk.append(int(row[5]))
    lows_sk.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates_sk.append(converted_date)

# death valley file
open_file = open("death_valley_2018_simple.csv", "r")
csv_file = csv.reader(open_file, delimiter=",")
header_row = next(csv_file)

highs_dv = []
lows_dv = []
dates_dv = []

for row in csv_file:
    try:
        high_dv = int(row[4])
        low_dv = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(converted_date)

# output
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)

ax[0].plot(dates_sk, highs_sk, c="red")
ax[0].plot(dates_sk, lows_sk, c="blue")

ax[1].plot(dates_dv, highs_dv, c="red")
ax[1].plot(dates_dv, lows_dv, c="blue")

fig.autofmt_xdate()

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.tick_params(axis="both", labelsize=12)
# plt.fill_between(dates_sk, highs_sk, lows_sk, facecolor="blue", alpha=0.1)

plt.show()