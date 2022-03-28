from core import rq
from data.transformers.name_transformer import NameTransformer
from data.transformers.service_transformer import ServiceTransformer
from services.city_extractor_service import TELECOM_FILE, CODE_NAME_FILE, fetch_city, NETWORK_WITH_CITY_FILE, \
    CITY_MAP_FILE


def prepare_data():
    NameTransformer(input_file=TELECOM_FILE, output_file=CODE_NAME_FILE).transform()
    fetch_city()
    ServiceTransformer(input_file=NETWORK_WITH_CITY_FILE, output_file=CITY_MAP_FILE).transform()


@rq.job(timeout=3600)
def get_city_for_networks():
    prepare_data()
