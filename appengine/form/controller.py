#!/usr/bin/env python

import webapp2, os, jinja2
from model import Model
from view import View

class Controller:
    print '1: Controller initialized'
    def __init__(self):
        model = Model()
        view = View()


jinja2_environment = jinja2.Environment(
    autoescape = True,
    loader = jinja2.FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__))))


class MainHandler(webapp2.RequestHandler):
    print '2: MainHandler initialized'
    def get(self):

        template_values = {
            'Welcome': 'Welcome to Carib'
        }
        template = jinja2_environment.get_template('form.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))

        self.response.write(review(self, do)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

