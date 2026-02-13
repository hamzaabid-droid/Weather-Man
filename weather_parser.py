import os
from datetime import datetime
from weather_record import WeatherRecord

class WeatherParser:
    @staticmethod
    def parse_file(filepath):
        records = []

        with open(filepath, "r") as file:
            lines = file.readlines()[1:]

            for line in lines:
                parts = line.strip().split(",")

                try:
                    if not parts[0]:
                        continue

                    date = datetime.strptime(parts[0], "%Y-%m-%d").date()
                    max_temp = parts[1]
                    min_temp = parts[3]
                    max_humidity = parts[7]
                    mean_humidity = parts[8]

                    if not all([max_temp, min_temp, max_humidity, mean_humidity]):
                        continue

                    record = WeatherRecord(
                        date=date,
                        max_temp=int(float(max_temp)),
                        min_temp=int(float(min_temp)),
                        max_humidity=int(float(max_humidity)),
                        mean_humidity=int(float(mean_humidity)),
                    )

                    records.append(record)

                except (ValueError, IndexError):
                    continue

        return records

    @staticmethod
    def parse_directory(dir_path):
        all_records = []

        for filename in os.listdir(dir_path):
            if filename.endswith(".txt"):
                full_path = os.path.join(dir_path, filename)
                all_records.extend(WeatherParser.parse_file(full_path))

        return all_records
