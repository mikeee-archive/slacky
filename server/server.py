import tornado.web
import tornado.ioloop

# RootHandler is the default endpoint called and returns a default message
class RootHandler(tornado.web.RequestHandler):
    def get(self):
        body = {'message': 'hello world'}
        self.write(body)

# HealthCheckHandler is an endpoint that returns the status of the server, can be used as a monitoring endpoint
class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        status = self._checkhealth()
        body = {'status': '%s' % status}
        self.write(body)
    def _checkhealth(self):
        return 'ok'
        

def Server():
    return tornado.web.Application([
        (r"/", RootHandler),
        (r"/health", HealthCheckHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path':'static'}) # cruft... TODO: implement a proper method of handling static files
    ])

def Run(port):
    server = Server()
    server.listen(port)
    tornado.ioloop.IOLoop.current().start()