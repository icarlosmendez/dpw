#!/usr/bin/env python

import webapp2, os, jinja2


jinja2_environment = jinja2.Environment(
    autoescape = True,
    loader = jinja2.FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__))))


class Controller(webapp2.RequestHandler):
    print '1: Controller initialized'
    def get(self):

        template_values = {
            'Welcome': 'Welcome to Carib'
        }
        template = jinja2_environment.get_template('form.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(template_values))
        self.response.write(template)


        if self.request.GET:
            companyName = self.request.GET['companyName']
            url = self.request.GET['url']
            launchDate = self.request.GET['launchDate']
            priName = self.request.GET['priName']
            priEmail = self.request.GET['priEmail']
            priPhone = self.request.GET['priPhone']
            priRole = self.request.GET['priRole']
            secName = self.request.GET['secName']
            secEmail = self.request.GET['secEmail']
            secPhone = self.request.GET['secPhone']
            secRole = self.request.GET['secRole']

            self.response.write(companyName + url + launchDate + priName + priEmail + priPhone + priRole + secName + secEmail + secPhone + secRole)

        else:
            pass
            self.response.write(template)



app = webapp2.WSGIApplication([
    ('/', Controller)
], debug=True)

