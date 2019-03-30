from tornado.web import RequestHandler


class JsonHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
