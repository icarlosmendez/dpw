import cgi

class Model():
    print '3: Model initialized'
    def __init__(self):
        self.do = FormDO()

        # instantiate FieldStorage function from the cgi class/module and set it to form
        self.do.form = cgi.FieldStorage()

        # capture company name
        self.do.companyName = self.do.form.getfirst('companyName', 'empty')
        # prevent script injection by escaping the user input
        self.do.companyName = cgi.escape(self.do.companyName)




class FormDO():
    print '4: FormDO initialized'
    def __init__(self):
        self.form = []
        self.companyName = ''
        self.url = ''
        self.launch = ''
        self.priName = ''
        self.priEmail = ''
        self.priPhone = ''
        self.priRole = ''
        self.secName = ''
        self.secEmail = ''
        self.secPhone = ''
        self.secRole = ''
