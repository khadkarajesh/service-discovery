import json
from pathlib import Path

from data.transformer import CITY_MAP_FILE


def get_services(city: str) -> dict:
    with open(Path.cwd() / 'data' / CITY_MAP_FILE, "r") as file:
        services = json.load(file)
        return services.get(city.lower())
