
from date_utils import format_date, get_month_name


class ReportPrinter:
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    
    
    def print_yearly_extremes(self, highest, lowest, humid):
        print(f"Highest: {highest.max_temp:02d}C on {format_date(highest.date)}")
        print(f"Lowest: {lowest.min_temp:02d}C on {format_date(lowest.date)}")
        print(f"Humidity: {humid.mean_humidity}% on {format_date(humid.date)}")

    def print_monthly_averages(self, avg_high, avg_low, avg_hum):
            print(f"Average Highest Temperature: {avg_high}C")
            print(f"Average Lowest Temperature: {avg_low}C")
            print(f"Average Mean Humidity: {avg_hum}%")

    def print_yearly_extremes(self,):
      
        pass

    def print_monthly_averages(self, ):
   
        pass

    def print_daily_chart(self, ):
     
        pass