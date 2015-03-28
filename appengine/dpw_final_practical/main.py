#
"""
Carlos Mendez
28MAR2015
DPW
Final Practical
"""
#
import webapp2
from function import Average, WebPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = WebPage()
        grades = []
        average = Average()

        if self.request.GET:
            name = self.request.GET['student']
            grade01 = (int(self.request.GET['grade01']))
            grade02 = (int(self.request.GET['grade02']))
            grade03 = (int(self.request.GET['grade03']))
            grades = [grade01, grade02, grade03]

            average = average.get_avg(grades)


            page.body = "<h1>Student name: {name}</h1>" \
                        "<h1>Individual Grades: {grade01}, {grade02}, {grade03}</h1>"\
                        "<h1>Average Grade: {average}</h1>"

            page.body = page.body.format(**locals())


        else:
            page.body = """
            <form method='get' action=''>
                <ul>
                    <li><label>Name: </label><input type='text' name='student' id='student'/></li>
                    <li><label>Grade 1: </label><input type='text' name='grade01' id='grade01'/></li>
                    <li><label>Grade 2: </label><input type='text' name='grade02' id='grade02'/></li>
                    <li><label>Grade 3: </label><input type='text' name='grade03' id='grade03' /></li>
                    <input type='submit' value='submit' />
                </ul>
            </form>
            """
        page.title = 'Student Avg'

        self.response.write(page.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
