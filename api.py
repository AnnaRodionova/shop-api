from tornado.web import Application

from handlers.companies import CompaniesHandler
from handlers.employees import EmployeesHandler
from handlers.products import ProductsHandler


def make_api():
    return Application([(r"/api/companies", CompaniesHandler),
                        (r"/api/employees", EmployeesHandler),
                        (r"/api/products", ProductsHandler)],
                       debug=True)
