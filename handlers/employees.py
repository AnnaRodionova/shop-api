import json

from .json_handler import JsonHandler


class EmployeesHandler(JsonHandler):
    def get(self):
        return self.write(json.dumps([{"emp": "Emp1"}, {"emp": "Emp2"}]))

    def post(self):
        return self.write(json.dumps({"emp": "Name"}))