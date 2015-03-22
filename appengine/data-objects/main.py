# Data objects allow us to treat a class as a holder for data.
# Dictionaries in Python are another option.
# JSON is an example in JavaScript

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # below are examples of data objects
        # this example was given by Rebecca on the course videos
        # nice and simple and quite different from Scott's version of a data object
        # I would personally refer to these objects as instances of the Character() class

        luke = Character()
        luke.name = 'Luke Skywalker'
        luke.profession = 'Jedi Knight'
        luke.age = 26
        luke.home_planet = 'Tattooine'

        leia = Character()
        leia.name = 'Princess Leia'
        leia.profession = 'Princess'
        leia.age = luke.age
        leia.home_planet = 'Alderan'

        yoda = Character()
        yoda.name = 'Master'
        yoda.profession = 'Jedi Master'
        yoda.age = 800
        yoda.home_planet = 'Dagobah'

        # you can assemble these data objects together into a list as below
        # this can provide portability and accessibility of the attributes
        chars = [luke, leia, yoda]

        # using a combination of bracket syntax and dot notation
        # you can drill down into the object
        print chars[1].profession


class Character(object):
    def __init__(self):
        self.name = ''
        self.profession = ''
        self.age = 0
        self.home_planet = ''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
