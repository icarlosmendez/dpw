
# this file used to be named person.py
# this id an example of class inheritance as explained by Rebecca in the video
# of primary importance is the initialization of the super class
# in Python3 you pass in 'object' as an argument to Person
# Person is inheriting from the generic 'object' uber-class
# Sounds like the proto_ object in JavaScript


class Person(object):
    def __init__(self):
        print 'Person created'
        self.name = ''
        self.age = 0
        self.language = ''

    def talk(self):
        print 'I am speaking in ' + self.language


# Now for the first example of inheritance
# When instantiating the sub-class of Student
# we pass in Person as the super-class
class Student(Person):
    # Per standard protocol, initialize the class
    def __init__(self):
        # Now there are two ways to invoke the inheritance of traits from the super-class
        # First is simply by calling Person with the init method and passing in self
        # Second way is below in sub-class Freshman()
        Person.__init__(self)
        self.college = ''
        self.language = ''


# Here again we're going to instantiate a sub-class
# and we'll be passing in the class Student from above as the super-class
# This makes Student both a sub and super-class
class Freshman(Student):
    def __init__(self):
        # Or you can call the super-class constructor function
        # and have the sub-class be the first argument as below
        # followed by the init function
        # The first one is shorter but the second one is more syntactically obvious
        super(Student, self).__init__()
        self.major = ''
        print self.name + ' speaks ' + self.language
        print self.name + ' is studying ' + self.major + ' at ' + self.college







# Everything below here is without specific purpose relative to inheritance
# It got there during multiple refactorings before the top of this page came together

# def Bob(self):
#     self.name = 'Bob'
#     self.learn = 'Web Design'
#     self.college = 'Full Sail'
#     self.language = 'Spanish'


# f = Freshman()
# print f

# stud2 = Student()
# stud2.name = 'Joe'
# stud2.learn = 'Web Development'
# stud2.language = 'French'

# stud = Person()

# Person()
# Student()
