import os
from datetime import datetime
from weather_records import WeatherRecord


class WeatherParser:
    
    @staticmethod
    def parse_file(filepath):
        records = []
        with open(filepath, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:  
                parts = line.strip().split(",")

    @staticmethod
    def parse_directory(dir_path):

        pass