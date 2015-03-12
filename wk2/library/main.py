from library import Student, Printer

class Controller:
    def __init__(self):

        # define the variable model as Student class function call
        model = Student()
        # define the variable view as Printer class function call
        view = Printer()

        # Bring the output of the Student class back into the controller
        # This allows us to then send it to the Printer class
        # 'data' receives the results of the make_student function
        # the variable new_student is returned by get_student_data
        data = model.get_student_data()

        # assign the value 'data' in the Printer class
        # the results of get_student_data()
        view.data = data
        # call the print_out() function of the Printer class
        view.print_out()

controller = Controller()

