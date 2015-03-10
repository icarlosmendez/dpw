
from library import Student
from library import Printer
# import library

class MainHandler:
    def __init__(self):
        Student.name = raw_input('Student name :')
        Student.degree = raw_input('Student degree :')
        Student.grades = raw_input('Student grades :')


MainHandler()
Printer(Student)

