#

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # instantiate Page() class and assign it to p
        p = Page()
        if self.request.GET:
            name = self.request.GET['user']
            age = self.request.GET['age']
            user_data = name + age
            p.body = "<h1>New user name: {name}\n Age: {age}</h1>"
            p.body = p.body.format(**locals())

        else:
            # get the body attribute of the Page() class and assign the right side of the equation to it
            p.body = """
            <form method='get' action=''>
                <label>Name: </label><input type='text' name='user' />
                <label>Age: </label><input type='text' name='age' />
                <input type='submit' value='submit' />
            </form>
            """
        p.title = 'Bobs'

        self.response.write(p.print_out())


class Page(object):
    def __init__(self):
        self.title =''
        self.css = "css/styles.css"

        self.head = """
<!doctype HTML>
<html>
<head>
    <title>{self.title}</title>
    <link href="{self.css}" rel='stylesheet' />
</head>
</html>
    <body>
"""
        self.body = ''
        self.close = """
    </body>
</html>

"""

    def print_out(self):
        html = self.head + self.body + self.close
        html = html.format(**locals())
        return html



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
