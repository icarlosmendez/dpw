
class Model:
    def __init__(self):
        print 'Model created'
        self.do = Movie_DO()
        self.do.title = 'Star Wars'
        self.do.cast = ['Ford', 'Fisher']
        self.do.rating = 'PG'

    def get_data(self):
        print 'Getter created'
        return self.do


class View:
    def __init__(self):
        print 'View created'
        self.data = None

    def print_out(self):
        print self.data


class Movie_DO:
    def __init__(self):
        print 'Do created'
        self.title = ''
        self.cast = []
        self.rating = ''