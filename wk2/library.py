
class Student:
    # initialize the constructor function
    def __init__(self, n, d, g):
        # create a variable for new student
        new_student = []
        # define the attributes
        self.name = n
        self.degree = d
        self.grades = g
        self.average = ''
        # append the attributes to new_student list
        new_student.append(n)
        new_student.append(d)
        new_student.append(g)
        new_student.append(avg(self))

# create a method to calculate average grade
def avg(self):
    # create a variable to hold the sum of all grades
    grade_avg = 0
    # iterate over list
    for i in self.grades:
        # add each new index value to variable
        grade_avg += i
    # create another variable to assign the average to
    average = grade_avg/len(self.grades)
    # return new variable with average grade
    return average

class Printer:
    # initialize Printer class constructor function
    def __init__(self, new_student):
        # test function is working
        print "Printer Class initialized"
        # print individual attributes from Student class
        print "Student's name is: " + new_student.name
        print "Student's degree is: " + new_student.degree
        print "Student's grades are: " + new_student.grades
        print "Student's average is: " + new_student.average

