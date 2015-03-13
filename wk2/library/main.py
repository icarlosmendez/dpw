from library import Student, Printer

class Controller:
    def __init__(self):
        # define the variable model as Student class function call
        model = Student()
        # define the variable view as Printer class function call
        view = Printer()
        # call the print_out method of 'view' which represents Printer class
        # passing in the the do property of model which represents Library class
        view.print_out(model.do)

controller = Controller()

