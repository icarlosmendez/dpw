
class View():
    def __init__(self):
        print '5: View initialized'
        pass

    def review(self, do):
        print '6: review initialized'
        for attr, value in do.__dict__.iteritems():
            print attr, value

