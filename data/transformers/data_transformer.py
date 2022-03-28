import json
from abc import ABC, abstractmethod


class DataTransformer(ABC):
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.data = {}

    def _save(self):
        with open(self.output_file, "w") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def _extract(self):
        pass
