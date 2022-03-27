import json

from services.city_extractor_service import map_code_to_name


class DataTransformer:
    def __init__(self, input_file, output_file):
        self.city_telecom = {}
        self.input_file = input_file
        self.output_file = output_file

    def _save(self):
        with open(self.output_file, "w") as f:
            json.dump(self.city_telecom, f, ensure_ascii=False, indent=2)

    def transform(self):
        self._extract_service_provider()
        self._save()

    def _extract_service_provider(self):
        with open(self.input_file) as f:
            for line in f:
                line = line.rstrip()
                data = line.split(";")
                city = data[-1].lower()
                name = map_code_to_name(data[0])
                if city:
                    if city in self.city_telecom:
                        self.city_telecom[city][name] = {
                            "2G": data[3] == '1',
                            "3G": data[4] == '1',
                            "4G": data[4] == '1'
                        }
                    else:
                        self.city_telecom[city] = {
                            name: {
                                "2G": data[3] == '1',
                                "3G": data[4] == '1',
                                "4G": data[4] == '1'
                            }
                        }
