import json
import os


class JsonReader:

    @staticmethod
    def read(file_name):

        file_path = os.path.join(
            "testdata",
            file_name
        )

        with open(file_path, "r") as file:

            return json.load(file)