
class Student:
    # initialize the constructor function
    def __init__(self):
        self.make_student()


    def make_student(self):
        # create a variable for new student
        self.new_student = []

        # define the basic attributes
        self.name = raw_input('Student name: ')
        self.degree = raw_input('Student degree: ')

        # grades is a list populated by a for loop
        # user input is collected using raw_input
        self.grades = []
        for i in range(1, 4):
            self.grades.append(raw_input('Enter a grade: '))

        # average uses the grades variable to output the GPA
        self.average = []
        self.average = self.avg(self.grades)

        # append all relevant inputs to new_student list
        self.new_student.append(self.name)
        self.new_student.append(self.degree)
        self.new_student.append(self.average)


    def get_student_data(self):
        # make new_student available to other functions
        # in this case that is the Printer class
        return self.new_student


    # create a method to calculate average grade
    def avg(self, grades):
        # create a variable to hold the output of avg()
        average = 0
        # iterate over list
        for i in self.grades:
            # add each new index value to variable average
            # convert i to an integer each time before adding to average
            average += int(i)
        # calculate the average and reassign new value to variable average
        average = average/len(self.grades)
        # return new variable with average grade
        return average


class Printer:
    # initialize Printer class constructor function
    def __init__(self):
        # data is a variable created in the controller
        # data is the culmination of make_student and get_student_data
        # establishing the variable of data provides a location for
        # the values from new_student to be passed into the Printer class
        self.data = None


    def print_out(self):
        # print individual attributes from variable new_student
        print '%s who is enrolled in the %s degree program has earned a GPA of %s.' % (self.data[0], self.data[1], self.data[2])
