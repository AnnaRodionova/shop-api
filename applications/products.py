from tornado.web import Application

from handlers.products import ProductsHandler, ProductHandler


def make_app():
    return Application([(r'/api/products', ProductsHandler),
                        (r'/api/products/([^/]+)', ProductHandler)])
