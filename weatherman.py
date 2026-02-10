import argparse
import os
from datetime import datetime

# ----------------- Argument Parser -----------------
parser = argparse.ArgumentParser(description="Weather Record Program - Multiple Reports")
parser.add_argument("path", help="Folder path of weather files")
parser.add_argument("-e", "--date", help="Year / Year-Month / Year-Month-Day")
parser.add_argument("-a", "--month", help="Year/Month for monthly averages")
parser.add_argument("-c", "--chart", help="Year-Month for monthly temperature chart")
args = parser.parse_args()

records = []
for filename in os.listdir(args.path):
    full_path = os.path.join(args.path, filename)
    if not os.path.isfile(full_path):
        continue
    with open(full_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 4 or parts[1] == "" or parts[2] == "" or parts[3] == "":
                continue
            try:
                date = parts[0].replace("/", "-")
                high = int(parts[1])
                low = int(parts[2])
                hum = int(parts[3])
                records.append((date, high, low, hum))
            except ValueError:
                continue
if args.date:
    max_temp = -1000
    min_temp = 1000
    max_humidity = -1
    max_temp_date = ""
    min_temp_date = ""
    max_humidity_date = ""
    found = False

    for date, high, low, hum in records:
        if date.startswith(args.date.replace("/", "-")):
            found = True
            if high > max_temp:
                max_temp = high
                max_temp_date = date
            if low < min_temp:
                min_temp = low
                min_temp_date = date
            if hum > max_humidity:
                max_humidity = hum
                max_humidity_date = date

    if found:
        try:
            dt = datetime.strptime(max_temp_date, "%Y-%m-%d")
            max_temp_date_fmt = dt.strftime("%B %d")
        except:
            max_temp_date_fmt = max_temp_date

        try:
            dt = datetime.strptime(min_temp_date, "%Y-%m-%d")
            min_temp_date_fmt = dt.strftime("%B %d")
        except:
            min_temp_date_fmt = min_temp_date

        try:
            dt = datetime.strptime(max_humidity_date, "%Y-%m-%d")
            max_humidity_date_fmt = dt.strftime("%B %d")
        except:
            max_humidity_date_fmt = max_humidity_date
        print("\n")
        print(f"Highest temperature: {max_temp}C on {max_temp_date_fmt}")
        print(f"Lowest temperature: {min_temp}C on {min_temp_date_fmt}")
        print(f"Highest humidity: {max_humidity}% on {max_humidity_date_fmt}")
    else:
        print(f"\nNo weather data found for {args.date}")

if args.month:
    total_high = 0
    total_low = 0
    total_humidity = 0
    count = 0
    month_input = args.month.replace("/", "-")

    for date, high, low, hum in records:
        if date.startswith(month_input):
            total_high += high
            total_low += low
            total_humidity += hum
            count += 1

    if count > 0:
        avg_high = round(total_high / count)
        avg_low = round(total_low / count)
        avg_humidity = round(total_humidity / count)
        print("\n")
        print("Average Highest Temperature:", f"{avg_high}C")
        print("Average Lowest Temperature:", f"{avg_low}C")
        print("Average Mean Humidity:", f"{avg_humidity}%")
    else:
        print(f"\nNo weather data found for {args.month}")

if args.chart:
    chart_input = args.chart.replace("/", "-")
    try:
        year_str, month_str = chart_input.split("-")
        year = int(year_str)
        month = int(month_str)
        month_name = datetime(year, month, 1).strftime("%B")
    except:
        print("\nInvalid chart argument. Use YYYY/MM or YYYY-MM format.")
        exit(1)

    daily_highs = {}
    daily_lows = {}

    for date, high, low, hum in records:
        if date.startswith(f"{year}-{month}"):
            day = date.split("-")[-1]
            daily_highs[day] = high
            daily_lows[day] = low

    if daily_highs:
        for day in sorted(daily_highs.keys(), key=lambda x: int(x)):
            day_fmt = day.zfill(2)
            print("\n")
            print(f"{day_fmt} \033[91m{'+' * daily_highs[day]}\033[0m {daily_highs[day]}C")
            print(f"{day_fmt} \033[94m{'+' * daily_lows[day]}\033[0m {daily_lows[day]}C")
    else:
        print(f"\nNo weather data found for {month_name} {year}")
