import re

from data.transformers.data_transformer import DataTransformer


class NameTransformer(DataTransformer):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def transform(self):
        self._extract()
        self._save()

    def _extract(self):
        with open(self.input_file) as f:
            for line in f:
                line = line.rstrip()
                code = line.split(",")[3]
                name = line.split(",")[2]
                name = re.sub(r'\([^()]*\)', '', name)
                self.data[code] = name.strip()
