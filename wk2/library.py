
class Student:
    # initialize the constructor function
    def __init__(self):
        print 'Student initialized'
        self.make_student()


    def make_student(self):
        # create a variable for new student
        self.new_student = []
        self.average = []
        # define the attributes

        self.name = raw_input('Student name: ')
        self.degree = raw_input('Student degree: ')
        # self.grades = [90, 50, 100]
        self.grades = []
        for i in range(1, 4):
            self.grades.append(raw_input('Enter a grade: '))
        self.average = self.avg(self.grades)

        self.new_student.append(self.name)
        self.new_student.append(self.degree)
        self.new_student.append(self.average)


    def get_student_info(self):
        return self.new_student


    # create a method to calculate average grade
    def avg(self, grades):
        # create a variable to hold the sum of all grades
        average = 0
        # iterate over list
        for i in self.grades:
            # add each new index value to variable
            average += int(i)
        # create another variable to assign the average to
        average = average/len(self.grades)
        # return new variable with average grade
        # print "%s's average is " + str(average) % self.name
        return average


class Printer:
    # initialize Printer class constructor function
    def __init__(self):
        print 'Printer initialized'
        self.data = None


    def print_out(self):
        # print individual attributes from Student class
        print '%s who is enrolled in %s degree program has a GPA of %s.' % (self.data[0], self.data[1], self.data[2])
