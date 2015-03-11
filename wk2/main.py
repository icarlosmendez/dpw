from library import Student, Printer

class MainHandler:
    def __init__(self):
        print 'MainHandler initialized'

        model = Student()
        view = Printer()
        data = model.get_student_info()
        view.data = data
        view.print_out()

main = MainHandler()

