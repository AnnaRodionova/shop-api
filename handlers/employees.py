import json

from .json_handler import JsonHandler


class EmployeesHandler(JsonHandler):
    def get(self):
        return self.write(json.dumps([{"emp": "Emp1"}, {"emp": "Emp2"}]))

    def post(self):
        return self.write(json.dumps({"emp": "Name"}))


class EmployeeHandler(JsonHandler):
    def get(self, id):
        return self.write(json.dumps([{"id": id, "emp": "Emp"}]))

    def delete(self, id):
        return self.write(json.dumps([{"id": id, "emp": "Emp"}]))

    def patch(self, id):
        return self.write(json.dumps([{"id": id, "emp": "Emp"}]))
