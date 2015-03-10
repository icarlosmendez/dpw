from library import Student, Printer

class MainHandler:
    def __init__(self):
        print 'MainHandler initialized'

        self.model = Student()
        self.view = Printer()

        self.view.print_out()

main = MainHandler()

