import concurrent.futures
import csv
import json
import logging
import re
from pathlib import Path

from services.location_service import LocationService
from utils import lamber93_to_gps

DATA_PATH = Path.cwd() / 'data'
CITY_MAP_FILE = DATA_PATH / "city_map.json"
CODE_NAME_FILE = DATA_PATH / "code_name.json"
NETWORK_WITH_CITY_FILE = DATA_PATH / "networks_with_city.txt"
TELECOM_FILE = DATA_PATH / "telecom.csv"
NETWORK_FILE = DATA_PATH / "networks_temp.csv"

location_service = LocationService()


def get_city(line):
    data = line.split(";")
    x, y = data[1], data[2]
    longitude, latitude = lamber93_to_gps(x, y)
    payload = location_service.reverse(longitude=longitude, latitude=latitude)
    if payload and len(payload.get('features')):
        row = f"{line.rstrip()};{payload.get('features')[0].get('properties').get('city')}\n"
        return row
    logging.error(f"failed to get city for {line}")
    return ''


def fetch_city():
    with open(NETWORK_FILE) as f:
        csv_file = csv.reader(f)
        next(csv_file)
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            result = list(executor.map(get_city, f.readlines()))
            with open(NETWORK_WITH_CITY_FILE, "w") as file_with_city:
                file_with_city.writelines(result)


def map_code_to_name(code):
    with open(CODE_NAME_FILE, "r") as file:
        mapper = json.load(file)
        return mapper.get(code)
