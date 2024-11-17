from src.exception import SensorException
from src.logger import logging
from src.utils import dump_csv_mongodb
import os
import sys

    
if __name__ == '__main__':
    try:
        filepath = r"C:\Users\Sidhi Gupta\Desktop\PROJECTS\Air Pressure Sensor Detection\notebook"
        database_name = "livesensor"
        collection_name = "sensor"
        dump_csv_mongodb(filepath,database_name,collection_name)

    except Exception as e:
        print(e)