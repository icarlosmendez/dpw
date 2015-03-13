# Student class
class Student:
    # initialize the constructor function
    def __init__(self):
        # initialize the StudentDO class
        # all attributes will be members of the StudentDO class
        # they will be prefixed with the .do method
        self.do = StudentDO()

        # define the basic attributes
        self.do.name = raw_input('Student name: ')
        self.do.degree = raw_input('Student degree: ')

        # grades is a list populated by a for loop
        # user input is collected using raw_input
        self.do.grades = []
        # then with a for range loop we accept 3 inputs
        # appending each to the 'grades' list
        # input =
        for i in range(1, 4):
            self.do.grades.append(raw_input('Enter a grade: '))

        # average uses the grades variable to output the GPA
        self.do.average = []
        self.do.average = self.avg(self.do.grades)

    # create a method to calculate average grade
    def avg(self, grades):
        # create a variable to hold the output of avg()
        average = 0
        # iterate over list
        for i in self.do.grades:
            # add each new index value to variable 'average'
            # convert i to an integer each time before adding to 'average'
            average += int(i)
        # calculate the average and reassign new value to variable 'average'
        average = average/len(self.do.grades)
        # return new variable with average grade
        return average


class StudentDO:
    def __init__(self):
        self.name = ''
        self.degree = ''
        self.grades = []
        self.average = []


class Printer:
    # initialize Printer class constructor function
    def __init__(self):
        pass

    def print_out(self, do):
        # print individual attributes from variable 'new_student' now known as 'data'
        # print '%s who is enrolled in the %s degree program has earned a GPA of %s.' % (self.data[0], self.data[1], self.data[2])
        for attr, value in do.__dict__ .iteritems():
            print attr, value

