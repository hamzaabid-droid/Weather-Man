import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description="Weather Record Program - Monthly Temperature Chart")
parser.add_argument("path", help="Folder path of weather files")
parser.add_argument("-c", "--chart", required=True, help="Year-Month")
args = parser.parse_args()

chart_input = args.chart.replace("/", "-")
year_str, month_str = chart_input.split("-")
year = int(year_str)
month = int(month_str)
month_name = datetime(year, month, 1).strftime("%B")

daily_highs = {}
daily_lows = {}

for filename in os.listdir(args.path):
    full_path = os.path.join(args.path, filename)
    if not os.path.isfile(full_path):
        continue
    with open(full_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 4 or parts[1] == "" or parts[2] == "":
                continue
            date = parts[0].replace("/", "-")
            if date.startswith(f"{year}-{month}"):
                day = date.split("-")[-1]
                try:
                    daily_highs[day] = int(parts[1])
                    daily_lows[day] = int(parts[2])
                except ValueError:
                    continue

def draw_bar(value, color):
    return f"{color}{'+' * value}\033[0m"

if daily_highs:
    print(f"{month_name} {year}")
    for day in sorted(daily_highs.keys(), key=lambda x: int(x)):
        day_fmt = day.zfill(2)
        print(f"{day_fmt} {draw_bar(daily_highs[day], '\033[91m')} {daily_highs[day]}C")
        print(f"{day_fmt} {draw_bar(daily_lows[day], '\033[94m')} {daily_lows[day]}C")
else:
    print(f"No weather data found for {month_name} {year}")