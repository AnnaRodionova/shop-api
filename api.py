from tornado.routing import RuleRouter, Rule, PathMatches

from applications.companies import make_app as make_companies_app
from applications.employees import make_app as make_employees_app
from applications.products import make_app as make_products_app


def make_api():
    companies_app = make_companies_app()
    employees_app = make_employees_app()
    products_app = make_products_app()

    return RuleRouter([
        Rule(PathMatches('/api/companies.*'), companies_app),
        Rule(PathMatches('/api/employees.*'), employees_app),
        Rule(PathMatches('/api/products.*'), products_app),
    ])
