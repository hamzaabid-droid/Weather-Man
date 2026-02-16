from datetime import datetime
import calendar

def format_date(date_obj):
    return date_obj.strftime("%B %d")

def get_month_name(month):
    return calendar.month_name[month]

def parse_year_month(value):
    if "/" in value:
        y, m = value.split("/")
    elif "-" in value:
        y, m = value.split("-")
    else:
        raise ValueError("Invalid date format")

    return int(y), int(m)
