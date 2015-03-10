from mod import *

class Cont:
    def __init__(self):
        print 'Cont created'
        m = Model()
        v = View()
        data = m.get_data()
        v.data = data
        v.print_out()

controller = Cont()
