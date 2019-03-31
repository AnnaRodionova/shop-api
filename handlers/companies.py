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


class CompanyHandler(JsonHandler):
    def get(self, id):
        return self.write(json.dumps({"id": id, "name": "Company"}))

    def delete(self, id):
        return self.write(json.dumps({"id": id, "name": "Company"}))

    def patch(self, id):
        return self.write(json.dumps({"id": id, "name": "Company"}))
