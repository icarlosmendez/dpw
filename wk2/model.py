
class Model:
    def __init__(self):
        print 'Model is instantiated!'
        self.create_movie()

    def create_movie(self):
        self.movie_info = []
        self.title = 'Star wars'
        self.cast = ['Ford', 'Hammil', 'Fisher']
        self.dates = '1977'
        self.director = 'Lucas'
        self.rating = 'PG'

        self.movie_info.append(self.title)
        self.movie_info.append(self.cast)
        self.movie_info.append(self.dates)
        self.movie_info.append(self.director)
        self.movie_info.append(self.rating)


    def get_movie_info(self):
        return self.movie_info

class View:
    def __init__(self):
        print 'View is instantiated!'
        self.data = None

    def print_out(self):
        print self.data
