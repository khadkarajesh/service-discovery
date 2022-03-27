from core import rq
from data.transformer import fetch_city


@rq.job(timeout=3600)
def get_city_for_networks():
    fetch_city()
