import tornado.web
import tornado.ioloop
import requests
import json

# RootHandler is the default endpoint called and returns a default message
class RootHandler(tornado.web.RequestHandler):
    def get(self):
        body = {'message': 'hello world'}
        self.write(body)

# HealthCheckHandler is an endpoint that returns the status of the server, can be used as a monitoring endpoint
class HealthCheckHandler(tornado.web.RequestHandler):
    """Returns the status of the connection with slack for a given token"""

    def initialize(self, slack_token):
        self.slack_token = slack_token

    def get(self):
        status, message, slack_team = self._checkhealth()
        body = {'status': '%s' % status, 'message': '%s' % message, 'slack_team': '%s' % slack_team}
        self.write(body)

    def _checkhealth(self):
        status = '503'
        message, slack_team = '', ''
        response = requests.get('https://slack.com/api/auth.test?token=%s' % self.slack_token)
        # TODO: Replace this sessions implementation with non-deprecated method.
        if response.json()['ok']:
            status = '200'
            slack_team = response.json()['team']
            message = "connected and authenticated with slack servers"
        return status, message, slack_team

class SlackMessageHandler(tornado.web.RequestHandler):
    """Post a new message to Slack"""

    def initialize(self, slack_token, api_key):
        self.slack_token = slack_token
        self.api_key = api_key

    def post(self):
        body = json.loads(self.request.body)
        if body.get('key') == self.api_key:
            payload = {
                'token':self.slack_token,
                'channel':body.get('channel'),
                'text':body.get('text'),
                'as_user':body.get('as_user')
            }  
            response = requests.post('https://slack.com/api/chat.postMessage', payload)
            status = '200'
            body = {'status': '%s' % status, 'response': '%s' % response.json()}
        else:
            status = '401'
            body = {'status': '%s' % status}
        self.write(body)

def router(slack_token, api_key):
    routes = [
        (r"/", RootHandler),
        (r"/health", HealthCheckHandler, {'slack_token': slack_token}),
        (r"/slack/message", SlackMessageHandler, {'slack_token': slack_token, 'api_key': api_key}),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path':'static'}) # cruft... TODO: implement a proper method of handling static files
    ]
    return tornado.web.Application(
        routes,
        slack_token=slack_token,
        api_key=api_key)

def Run(port, slack_token, api_key):
    server = router(slack_token, api_key)
    server.listen(port)
    tornado.ioloop.IOLoop.current().start()