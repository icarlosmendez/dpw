
class Person:
    def __init__(self):
        print 'Person created'
        self.name = ''
        self.ssn = 0
        self.language = ''

    def talk(self):
        print 'I am speaking in ' + self.language


class Student(Person):
    def learn(self):
        self.learn = ''

    def attend(self):
        self.college = ''

    def talk(self):
        self.language = ''


class Freshman(Student):
    def student(self):
        print self.name + ' speaks ' + self.language
        print self.name + ' is studying ' + self.learn + ' at ' + self.college





def Bob(self):
    self.name = 'Bob'
    self.learn = 'Web Design'
    self.college = 'Full Sail'
    self.language = 'Spanish'


f = Freshman()
print f

# stud2 = Student()
# stud2.name = 'Joe'
# stud2.learn = 'Web Development'
# stud2.language = 'French'




# stud = Person()


# Person()
# Student()
