__author__ = 'Carlos Mendez'

#define a class and write a constructor function
class Student:
    #constructor function here
    def __init__(self, n, g):
        print "student %s created" % n
        self.name = n
        self.gender = g
        self.grades = []


#method is the 4th member including the 3 properties
    def getAvg(self):
        total= 0
        for i in self.grades:
            total += i

        return total/len(self.grades)


