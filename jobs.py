from core import rq
from data.transformer import fetch_city, generate_code_name_mapper, DataTransformer, NETWORK_WITH_CITY_FILE, \
    CITY_MAP_FILE


@rq.job(timeout=3600)
def get_city_for_networks():
    generate_code_name_mapper()
    fetch_city()
    transformer = DataTransformer(input_file=NETWORK_WITH_CITY_FILE, output_file=CITY_MAP_FILE)
    transformer.transform()
