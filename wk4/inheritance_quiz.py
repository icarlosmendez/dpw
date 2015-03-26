#
"""
Carlos Mendez
25MAR2015
DPW
Inheritance, Abstraction and Polymorphism Quiz

"""

class AircraftCarrier(object):
    def __init__(self):
        self.power_plant = ''
        self.max_speed = 0
        self._armaments = []
        self.__crew = []

    def accelerates(self):
        pass

    def turns(self):
        pass

    def fights(self):
        pass

    @property
    def armaments(self):
        return self._armaments

    @armaments.setter
    def armaments(self, new_armament):
        self._armaments = new_armament



class F18Hornet(AircraftCarrier):
    def __init__(self):
        super(AircraftCarrier, self).__init__()
        self.power_plant = ''
        self.max_speed = 0
        self._armaments = []
        self.__crew = []
        self.afterburner = True
        self.tail_hook = True


    def accelerates(self):
        pass

    def turns(self):
        pass

    def fights(self):
        pass

    def climb_rate(self):
        pass



class SH60SeaHawk(AircraftCarrier):
    def __init__(self):
        super(AircraftCarrier, self).__init__()
        self.power_plant = ''
        self.max_speed = 0
        self._armaments = []
        self.__crew = []
        self.sonar_dipper = True
        self.wench = True

    def accelerates(self):
        pass

    def turns(self):
        pass

    def fights(self):
        pass

    def hovers(self):
        pass