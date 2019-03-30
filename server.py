import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.routing import PathMatches, Rule, RuleRouter
from tornado.web import Application

from api import make_api


def make_server():
    api = make_api()
    router = RuleRouter([Rule(PathMatches('/api/.*'), api)])
    return HTTPServer(router)


if __name__ == "__main__":
    server = make_server()
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
