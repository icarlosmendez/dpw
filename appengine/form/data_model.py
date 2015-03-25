import webapp2, cgi

class Form(object):
    print '3: Model initialized'
    def __init__(self):
        self.do = FormDO()

        # instantiate FieldStorage function from the cgi class/module and set it to form
        # self.do.form = cgi.FieldStorage()



class FormHandler(webapp2.RequestHandler, Form):
    def __init__(self):
        super(Form, self).__init__()

    def get(self):
        if self.request.GET:
            # capture company name
            self.do.companyName = self.request.GET['companyName']
            self.do.url = self.request.GET['url']
            self.do.launchDate = self.request.GET['launchDate']
            # prevent script injection by escaping the user input
            # self.do.companyName = cgi.escape(self.do.companyName)

        else:
            pass
            # self.response.write(template)



class FormDO():
    print '4: FormDO initialized'
    def __init__(self):
        self.form = []
        self.companyName = ''
        self.url = ''
        self.launchDate = ''
        self.priName = ''
        self.priEmail = ''
        self.priPhone = ''
        self.priRole = ''
        self.secName = ''
        self.secEmail = ''
        self.secPhone = ''
        self.secRole = ''
