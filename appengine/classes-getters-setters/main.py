#

import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # creating an instance of class of Page() and assigning it to template_page
        template_page = Page()
        # get the attribute title from Page() and assign the value 'Template'
        template_page.title = 'Template'
        template_page.css = 'css/style.css'
        template_page.body = "Welcome to my re-factored OOP Python page!<br />This is an HTML Template built with Python.<br />It is now using getters and setters"

        # self.response.write(template_page.print_out())

        self.response.write(template_page.update())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
