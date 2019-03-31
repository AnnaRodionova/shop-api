from tornado.web import Application

from handlers.companies import CompaniesHandler, CompanyHandler


def make_app():
    return Application([(r'/api/companies', CompaniesHandler),
                        (r'/api/companies/([^/]+)', CompanyHandler)])
