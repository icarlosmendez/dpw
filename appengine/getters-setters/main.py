#

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Tommy's grades
        t = Transcript()
        t.grade01 = 90
        t.grade02 = 100
        t.quiz01 = 75
        t.quiz02 = 99

        # Below we call the calc_grade function to do the math
        t.calc_grade()

        # ** This statement is calling the final_grade getter function below
        # and outputting the result to the browser
        self.response.write("Tommy's final grade is " + str(t.final_grade))

        # Sally's grades
        s = Transcript()
        s.grade01 = 45
        s.grade02 = 80
        s.quiz01 = 66
        s.quiz02 = 76

        # Below we call the calc_grade function to do the math
        s.calc_grade()

        # ** This statement is calling the final_grade getter function below
        # and outputting the result to the browser
        self.response.write("<br />Sally's final grade is " + str(s.final_grade))


class Transcript(object):
    def __init__(self):
        self.grade01 = 0
        self.grade02 = 0
        self.grade03 = 0
        self.quiz01 = 0
        self.quiz02 = 0
        self.final_exam = 0
        self.__final_grade = 0 # private attribute

    # the getter
    @property
    def final_grade(self):

        return self.__final_grade

    # the setter
    @final_grade.setter
    def final_grade(self, new_final_grade):
        self.__final_grade = new_final_grade


    def calc_grade(self):
        # calculate final grade
        self.__final_grade = (self.grade01 + self.grade02 + self.quiz01 + self.quiz02 + self.final_exam) /5


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
