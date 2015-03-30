#!/usr/bin/env python

import webapp2
from form import Form


class Controller(webapp2.RequestHandler):
    def get(self):

        form = Form()

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

            form.body = form.body.format(**locals())

            form.body = '''
            <fieldset class="fieldWrap"><!-- Master Fieldset -->
                <h3>Contact Information</h3>
                <fieldset>
                    <div id="company" class="left">
                        <h4>Your Company</h4>
                            <label>Company Name
                                <h5>{companyName}</h5></label>
                            <label>Current Or Desired URL
                                <h5>{url}</h5></label>
                            <label>Anticipated Launch Date
                                <h5>{launchDate}</h5></label>

                    </div>
                </fieldset>
            </fieldset>
            '''

        form.body = form.body.format(**locals())

        # else:
        #     form.body = ''

        form.title = 'Contact Info'
        self.response.write(form.print_out())


app = webapp2.WSGIApplication([
    ('/', Controller)
], debug=True)

