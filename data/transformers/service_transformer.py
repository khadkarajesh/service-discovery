from data.transformers.data_transformer import DataTransformer
from services.city_extractor_service import map_code_to_name


class ServiceTransformer(DataTransformer):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def transform(self):
        self._extract()
        self._save()

    def _extract(self):
        with open(self.input_file) as f:
            for line in f:
                line = line.rstrip()
                data = line.split(";")
                city = data[-1].lower()
                name = map_code_to_name(data[0])
                if city:
                    if city in self.data:
                        self.data[city][name] = {
                            "2G": data[3] == '1',
                            "3G": data[4] == '1',
                            "4G": data[4] == '1'
                        }
                    else:
                        self.data[city] = {
                            name: {
                                "2G": data[3] == '1',
                                "3G": data[4] == '1',
                                "4G": data[4] == '1'
                            }
                        }
