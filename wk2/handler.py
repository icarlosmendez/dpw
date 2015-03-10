from data import Data, Printer

# Main class is my Controller
class Main:
    def __init__(self):
        print 'Main created'
        # instantiate classes to provide access from Main
        self.model = Data()
        self.view = Printer()

        # create variable to store input data
        # grades = raw_input('Enter grades: ')
        # create variable to hold result of get_avg()
        avg = self.model.get_avg([10,20,30])

        # call print function and pass in avg argument
        # self.v.print_out(avg)

        # or which provides more explicit control of the presentation
        self.view.data = avg
        self.view.print_out()


controller = Main()
