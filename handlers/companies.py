import json

from .json_handler import JsonHandler


class CompaniesHandler(JsonHandler):
    def get(self):
        return self.write(
            json.dumps([{
                "name": "Company 1"
            }, {
                "name": "Company 2"
            }]))

    def post(self):
        return self.write(json.dumps({"name": "Company name"}))
