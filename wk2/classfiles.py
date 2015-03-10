__author__ = 'Carlos Mendez'

#this is the import statement
from objects import Student

#instantiation  of the Student object
carlos = Student("Carlos", "Male")

carlos.grades = [70,85,90]
print carlos.getAvg()
print carlos.name


