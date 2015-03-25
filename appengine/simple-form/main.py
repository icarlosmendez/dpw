#
"""
Carlos Mendez
24MAR2015
DPW
Simple Form
"""

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # the page variable will be used to hold the html that will make up the form
        page_head = '''
        <!doctype HTML>
            <html>
                <head>
                    <title>Simple Form</title>
                </head>
        '''
        page_body = '''
                <body>
                    <div></div>
                    <form method='GET'>
                        <label>Name: </label><input type='text' name='user' />
                        <label>Email: </label><input type='text' name='email' />
                        <input type='submit' value='submit' />
        '''
        page_close = '''
                    </form>
                </body>
            </html>
        '''

        # here we will get the data input by the user
        # first we use a conditional statement to see if there are any variables in the url
        # if false then bypass this statement
        if self.request.GET:
            # if true assign the values to these new variables user and email
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)

        # here we pass in the page variable to the write() method
        else:
            self.response.write(page_head + page_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
