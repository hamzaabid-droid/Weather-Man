import argparse
import os

parser = argparse.ArgumentParser(description="Weather Record Program")
parser.add_argument("path", help="Path of weatherfiles folder")
parser.add_argument("-d", "--date", help="Date in format")
args = parser.parse_args()

data_found=False

for file_name in os.listdir(args.path):
        file_path = os.path.join(args.path, file_name)
        with open(file_path, "r") as file:
            for line in file:
                values = line.strip().split(",")
                if values[0].startswith(args.date):
                    print("\nWeather Record Found")
                    print("File Name :", file_name)
                    print("Date      :", values[0])
                    print("Max Temp  :", values[1])
                    print("Min Temp  :", values[2])
                    print("Humidity  :", values[3], "%")
                    data_found = True
                    break

if not data_found:
    print("No weather data found for date")
