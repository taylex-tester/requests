import json
import os
from Util.basePath import base_path

json_file_path = os.path.join(base_path, "Config")


class ReadJson(object):
    @staticmethod
    def read(filename):
        file_path = os.path.join(json_file_path, filename)
        with open(file_path, "r", encoding="UTF-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def write(data, filename):
        file_path = os.path.join(json_file_path, filename)
        with open(file_path, "w", encoding="UTF-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_value(self, filename, key):
        return self.read(filename).get(key)


readJson = ReadJson()
print(type(readJson.get_value("return.json", "null")))

