import argparse

parser = argparse.ArgumentParser(description="Weatherman Program")

# required argument
parser.add_argument("path", help="Path to weather files directory")

# optional arguments
parser.add_argument("-e", "--year", help="Year (e.g. 2002)")
parser.add_argument("-d", "--date", help="Specific date (YYYY-MM-DD)")

args = parser.parse_args()

print("Path:", args.path)
print("Year:", args.year)
print("Date:", args.date)
