
# Data class is my Model
class Data:
    def __init__(self):
        print 'Data created'

    def get_avg(self, n):
        total = 0
        for i in n:
            total += i
        avg = total/len(n)
        return avg


# Printer class is my View
class Printer:
    def __init__(self):
        print 'Printer created'
        self.data = 0

    # def print_out(self, data):
    #     print 'The average is ' + str(data)

    def print_out(self):
        print 'The average is ' + str(self.data)


