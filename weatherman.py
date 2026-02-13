import argparse
from datetime import datetime
from weather_parser import WeatherParser
from report_printer import ReportPrinter
from date_utils import parse_year_month

class Weatherman:
    def __init__(self, data_dir):
        self.records = WeatherParser.parse_directory(data_dir)
        self.printer = ReportPrinter()
        
    def yearly_extremes(self, value):
        value = str(value)

        # Full date YYYY-MM-DD
        if "-" in value and value.count("-") == 2:
            date_obj = datetime.strptime(value, "%Y-%m-%d").date()
            records = [r for r in self.records if r.date == date_obj]
            if not records:
                print(f"No data for date {date_obj}")
                return
            rec = records[0]
            self.printer.print_yearly_extremes(rec, rec, rec)

        # Year and month YYYY/MM or YYYY-MM
        elif "/" in value or ("-" in value and value.count("-") == 1):
            year, month = parse_year_month(value)
            records = [r for r in self.records if r.date.year == year and r.date.month == month]
            if not records:
                print(f"No data for {year}/{month}")
                return
            max_rec = max(records, key=lambda r: r.max_temp)
            min_rec = min(records, key=lambda r: r.min_temp)
            humid_rec = max(records, key=lambda r: r.max_humidity)
            self.printer.print_yearly_extremes(max_rec, min_rec, humid_rec)

        # Only year YYYY
        else:
            year = int(value)
            year_records = [r for r in self.records if r.date.year == year]
            if not year_records:
                print(f"No data for year {year}")
                return
            max_rec = max(year_records, key=lambda r: r.max_temp)
            min_rec = min(year_records, key=lambda r: r.min_temp)
            humid_rec = max(year_records, key=lambda r: r.max_humidity)
            self.printer.print_yearly_extremes(max_rec, min_rec, humid_rec)

    def monthly_averages(self, year, month):
        records = [r for r in self.records if r.date.year == year and r.date.month == month]
        if not records:
            print(f"No data for {year}/{month}")
            return
        avg_max = sum(r.max_temp for r in records) // len(records)
        avg_min = sum(r.min_temp for r in records) // len(records)
        avg_hum = sum(r.mean_humidity for r in records) // len(records)
        self.printer.print_monthly_averages(avg_max, avg_min, avg_hum)

    def daily_chart(self, year, month):
        records = [r for r in self.records if r.date.year == year and r.date.month == month]
        self.printer.print_daily_chart(records, year, month)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-e", help="YEAR or YEAR/MONTH or FULL DATE")
    parser.add_argument("-a", help="YEAR/MONTH")
    parser.add_argument("-c", help="YEAR/MONTH")
    return parser.parse_args()

def main():
    args = parse_args()
    wm = Weatherman(args.path)

    if args.e:
        wm.yearly_extremes(args.e)
    if args.a:
        y, m = parse_year_month(args.a)
        wm.monthly_averages(y, m)
    if args.c:
        y, m = parse_year_month(args.c)
        wm.daily_chart(y, m)

if __name__ == "__main__":
    main()
