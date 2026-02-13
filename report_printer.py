from date_utils import format_date, get_month_name

class ReportPrinter:
    red = "\033[91m"
    blue = "\033[94m"
    reset = "\033[0m"

    def print_yearly_extremes(self, max_rec, min_rec, humid_rec):
        print(f"Highest: {max_rec.max_temp:02d}C on {format_date(max_rec.date)}")
        print(f"Lowest: {min_rec.min_temp:02d}C on {format_date(min_rec.date)}")
        print(f"Humidity: {humid_rec.max_humidity}% on {format_date(humid_rec.date)}\n")

    def print_monthly_averages(self, avg_max, avg_min, avg_hum):
        print(f"Average Highest Temperature: {avg_max}C")
        print(f"Average Lowest Temperature: {avg_min}C")
        print(f"Average Mean Humidity: {avg_hum}% \n")
        
    def print_daily_chart(self, records, year, month):
        if not records:
            print("No records to display for chart.")
            return

        print(f"\n{get_month_name(month)} {year}")
        records.sort(key=lambda r: r.date.day)

        for r in records:
            min_bar = "+" * r.min_temp
            max_bar = "+" * (r.max_temp - r.min_temp)
            print(
                f"{r.date.day:02d} "
                f"{self.blue}{min_bar}{self.reset}"
                f"{self.red}{max_bar}{self.reset} "
                f"{r.min_temp:02d}C - {r.max_temp:02d}C"
            )
