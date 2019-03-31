from tornado.web import Application

from handlers.employees import EmployeesHandler, EmployeeHandler


def make_app():
    return Application([(r'/api/employees', EmployeesHandler),
                        (r'/api/employees/([^/]+)', EmployeeHandler)])
