
class Student:
    print 'Student initialized'
    # initialize the constructor function
    def __init__(self):
        # create a variable for new student
        average = []
        # define the attributes
        self.do = Student_DO()
        self.name = raw_input('Student name :')
        self.degree = raw_input('Student degree :')
        self.grades = ['90, 80, 100']
        self.average = self.avg()

    # create a method to calculate average grade
    def avg(self):
        # create a variable to hold the sum of all grades
        average = 0
        # iterate over list
        for i in self.grades:
            # add each new index value to variable
            average += i
        # create another variable to assign the average to
        average = average/len(self.grades)
        # return new variable with average grade
        return average


class Printer:
    print 'Printer initialized'

    # initialize Printer class constructor function
    def __init__(self):

        # test function is working
        print "Printer Class initialized"
        self.data = None

    def print_out(self):
        # print individual attributes from Student class
        print self.data


class Student_DO:
    def __init__(self):
        print 'Data Object created'
        self.name = ''
        self.degree = ''
        self.grades = []
        self.average = ''