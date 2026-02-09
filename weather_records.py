import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser(description="Weather Record Program")
parser.add_argument("path", help="Folder path of weather files")
parser.add_argument("-e", "--date", required=True, 
                    help="Year / Year-Month / Year-Month-Day (e.g., 2004 or 2004-08 or 2004-08-15)")
args = parser.parse_args()

max_temp = -1000
min_temp = 1000
max_humidity = -1

max_temp_date = ""
min_temp_date = ""
max_humidity_date = ""

found = False

for filename in os.listdir(args.path):
    full_path = os.path.join(args.path, filename)
    if not os.path.isfile(full_path):
        continue

    with open(full_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 3 or parts[1] == "" or parts[2] == "" or parts[3] == "":
                continue
            
            date_str = parts[0]
            if date_str.startswith(args.date):
                found = True
                high = int(parts[1])
                low = int(parts[2])
                humidity = int(parts[3])

                if high > max_temp:
                    max_temp = high
                    max_temp_date = date_str
                
                if low < min_temp:
                    min_temp = low
                    min_temp_date = date_str
                
                if humidity > max_humidity:
                    max_humidity = humidity
                    max_humidity_date = date_str

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d")
    except ValueError:
        return date_str

if found:
    print(f"Highest temperature: {max_temp}C on {format_date(max_temp_date)}")
    print(f"Lowest temperature: {min_temp}C on {format_date(min_temp_date)}")
    print(f"Highest humidity: {max_humidity}% on {format_date(max_humidity_date)}")
else:
    print("No weather data found for", args.date)
