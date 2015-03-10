from model import Model, View

class Controller:
    def __init__(self):
        print 'Controller is instantiated!'
        model = Model()
        view = View()
        data = model.get_movie_info()
        view.data = data
        view.print_out()

controller = Controller()
print Model.create_movie()
