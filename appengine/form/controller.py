#!/usr/bin/env python

import webapp2, os, jinja2
from data_model import Form
from data_view import View


jinja2_environment = jinja2.Environment(
    autoescape = True,
    loader = jinja2.FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__))))


class Controller(webapp2.RequestHandler):
    print '2: MainHandler initialized'
    def get(self):

        model = Form()
        view = View()

        template_values = {
            'Welcome': 'Welcome to Carib'
        }
        self.template = jinja2_environment.get_template('form.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.template.render(template_values))

        self.response.write(self.template)
        # self.response.write(view.review(model.do))
        self.response.write(model.do)




app = webapp2.WSGIApplication([
    ('/', Controller)
], debug=True)

