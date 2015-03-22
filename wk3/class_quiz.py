# Custodian
class Custodian(object):
    def __init__(self):
        self.name = ''
        self.shift = bool
        self.dreams = []
        self._salary = 0
        self.__passion = None

    def trash_collection(self, refuse):
        three_pm_pickup = refuse
        return three_pm_pickup

    def pool_vacuuming(self, leaves_in_pool):
        wet_leaves = leaves_in_pool
        return wet_leaves

    def restrooms_cleaning(self, passed_out_junkie):
        if passed_out_junkie:
            problem = True
            return problem



# Soldier
class Soldier(object):
    def __init__(self):
        self.name = 'Gomer Pyle'
        self.rank = 'Sargeant'
        self._serial_number = 123456789
        self.__theater = ''
        self.sense_of_humor = True

    def eats(self):
        pass

    def sleeps(self):
        pass

    def cleans(self):
        pass


# Dairy Cow
class DairyCow(object):
    def __init__(self):
        self.breed = 'Tux'
        self.height = '140 cm'
        self.weight = '8 - 900 Kilos'
        self._origin = 'Tyrol, Austria'
        self.__prospects = 'Endangered'

    def breeding(self, offspring):
        spring = True
        while spring:
            offspring += 1
            return offspring

    def grazing(self, mountain_pasture):
        mountain_pasture = ''
        try:
            if mountain_pasture is 'green':
                graze()
        except:
            trough_feeding()

    def pooping(self, grass):
        dung = grass
        return dung
