import tornado.web
import tornado.ioloop

# RootHandler is the default endpoint called and returns a default message
class RootHandler(tornado.web.RequestHandler):
    def get(self):
        message = "You've found me!"
        body = {'message': '%s' % message}
        self.write(body)

# HealthCheckHandler is an endpoint that returns the status of the server, can be used as a monitoring endpoint
class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        status = 'ok'
        body = {'status': '%s' % status}
        self.write(body)

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