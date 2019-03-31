import json

from .json_handler import JsonHandler


class ProductsHandler(JsonHandler):
    def get(self):
        return self.write(json.dumps([{"prod": "Name1"}, {"prod": "Name2"}]))

    def post(self):
        return self.write(json.dumps({"prod": "Name"}))


class ProductHandler(JsonHandler):
    def get(self, id):
        return self.write(json.dumps({"id": id, "prod": "Name"}))

    def delete(self, id):
        return self.write(json.dumps({"id": id, "prod": "Name"}))

    def patch(self, id):
        return self.write(json.dumps({"id": id, "prod": "Name"}))