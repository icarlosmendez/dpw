# import webapp2

# class Form(object):
#     print '3: Model initialized'
#     def __init__(self):
#         self.do = FormDO()



# class FormHandler(webapp2.RequestHandler, Form):
#     def __init__(self):
#         super(Form, self).__init__()
#
#     def get(self):
#         if self.request.GET:
#             self.do.companyName = self.request.GET['companyName']
#             self.do.url = self.request.GET['url']
#             self.do.launchDate = self.request.GET['launchDate']
#             self.do.priName = self.request.GET['priName']
#             self.do.priEmail = self.request.GET['priEmail']
#             self.do.priPhone = self.request.GET['priPhone']
#             self.do.priRole = self.request.GET['priRole']
#             self.do.secName = self.request.GET['secName']
#             self.do.secEmail = self.request.GET['secEmail']
#             self.do.secPhone = self.request.GET['secPhone']
#             self.do.secRole = self.request.GET['secRole']
#
#         else:
#             pass
#             self.response.write(template)



# class FormDO():
#     print '4: FormDO initialized'
#     def __init__(self):
#         self.form = []
#         self.companyName = ''
#         self.url = ''
#         self.launchDate = ''
#         self.priName = ''
#         self.priEmail = ''
#         self.priPhone = ''
#         self.priRole = ''
#         self.secName = ''
#         self.secEmail = ''
#         self.secPhone = ''
#         self.secRole = ''



# class View():
#     def __init__(self):
#         print '5: View initialized'
#         pass
#
#     def review(self, do):
#         print '6: review initialized'
#         for attr, value in do.__dict__.iteritems():
#             print attr, value