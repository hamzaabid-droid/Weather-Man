import argparse
import os

# ------------------ Arguments ------------------
parser = argparse.ArgumentParser(description="Weather Data Analysis")
parser.add_argument("path", help="Folder containing weather data files")
parser.add_argument("-e", "--date", help="Show stats for a specific date (YYYY/MM/DD)")
parser.add_argument("-a", "--month", help="Show average stats for a month (YYYY/MM)")
parser.add_argument("-c", "--chart", help="Show temperature chart for a month (YYYY/MM)")
args = parser.parse_args()

# ------------------ Read all data ------------------
records = []  # stores (date, high_temp, low_temp, humidity)

for filename in os.listdir(args.path):
    filepath = os.path.join(args.path, filename)
    if not os.path.isfile(filepath):
        continue
    with open(filepath) as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue
            try:
                date = parts[0].replace("/", "-")
                high_temp = int(parts[1])
                low_temp = int(parts[2])
                humidity = int(parts[3])
                records.append((date, high_temp, low_temp, humidity))
            except ValueError:
                continue  # skip invalid lines

# ------------------ Daily stats (-e) ------------------
if args.date:
    target_date = args.date.replace("/", "-")
    max_temp = -999
    min_temp = 999
    max_humidity = -1
    max_temp_date = min_temp_date = max_humidity_date = ""

    for date, high, low, hum in records:
        if date.startswith(target_date):
            if high > max_temp:
                max_temp, max_temp_date = high, date
            if low < min_temp:
                min_temp, min_temp_date = low, date
            if hum > max_humidity:
                max_humidity, max_humidity_date = hum, date

    if max_temp_date:
        print("\n")
        print(f"Highest Temperature: {max_temp}C on {max_temp_date}")
        print(f"Lowest Temperature: {min_temp}C on {min_temp_date}")
        print(f"Highest Humidity: {max_humidity}% on {max_humidity_date}")

if args.month:
    target_month = args.month.replace("/", "-")
    total_high = total_low = total_humidity = count = 0

    for date, high, low, hum in records:
        if date.startswith(target_month):
            total_high += high
            total_low += low
            total_humidity += hum
            count += 1

    if count:
        print("\n")
        print(f"Average Highest Temperature: {round(total_high / count)}C")
        print(f"Average Lowest Temperature: {round(total_low / count)}C")
        print(f"Average Humidity: {round(total_humidity / count)}%")

if args.chart:
    year, month = map(int, args.chart.replace("/", "-").split("-"))
    daily_stats = {}

    for date, high, low, hum in records:
        y, m, d = map(int, date.split("-"))
        if y == year and m == month:
            if d not in daily_stats:
                daily_stats[d] = {"high": high, "low": low}
            else:
                daily_stats[d]["high"] = max(daily_stats[d]["high"], high)
                daily_stats[d]["low"] = min(daily_stats[d]["low"], low)

    print("\n")
    for day in sorted(daily_stats.keys()):
        low = daily_stats[day]["low"]
        high = daily_stats[day]["high"]

        blue_bar = "\033[94m" + "+" * low + "\033[0m"
        red_bar = "\033[91m" + "+" * (high - low) + "\033[0m"
        print(f"{str(day).zfill(2)} {blue_bar}{red_bar} {low:02d}C - {high}C")
