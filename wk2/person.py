
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
        print self.name + ' is learning '

    def attend(self):
        print self.name + ' is attending'

    def talk(self):
        super(language())
        print 'I LOVE PYTHON!'

stud1 = Student()
stud1.name = 'Bob'
stud1.learn = 'Web Design'
stud1.language = 'Spanish'

stud2 = Student()
stud2.name = 'Joe'
stud2.learn = 'Web Development'
stud2.language = 'French'


stud1.learn()
stud1.attend()

# stud2 = Student
# stud2.learn(Student)

