import argparse
import os

parser = argparse.ArgumentParser(description="Weather Record Program - Monthly Averages")
parser.add_argument("path", help="Folder path of weather files")
parser.add_argument("-a", "--month", required=True, help="Year/Month")
args = parser.parse_args()

total_high = 0
total_low = 0
total_humidity = 0
count = 0

for filename in os.listdir(args.path):
    full_path = os.path.join(args.path, filename)
    if not os.path.isfile(full_path):
        continue
    with open(full_path, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) < 4 or data[1] == "" or data[2] == "" or data[3] == "":
                continue
            date = data[0]
            month_input = args.month.replace("/", "-")
            if date.startswith(month_input):
                try:
                    high = int(data[1])
                    low = int(data[2])
                    hum = int(data[3])
                except ValueError:
                    continue
                total_high += high
                total_low += low
                total_humidity += hum
                count += 1

if count > 0:
    avg_high = round(total_high / count)
    avg_low = round(total_low / count)
    avg_humidity = round(total_humidity / count)
    print("Average Highest Temperature:", f"{avg_high}C")
    print("Average Lowest Temperature:", f"{avg_low}C")
    print("Average Mean Humidity:", f"{avg_humidity}%")
else:
    print("No weather data found for", args.month)
