# Buttons
# Introducing the use of classes in Python and Google app-engine

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # instantiating instances of the button class and
        # assigning them to variables about_button and contact_button
        about_button = Button()
        contact_button = Button()

        # calling the click() method from outside the Button() class using dot syntax
        about_button.click()

        # assigning a value to the label attribute inside the Button() class
        # while associating that inherited attribute via dot syntax
        # to separate methods inside the Button() class
        about_button.label = 'About Us'
        contact_button.label = 'Contact Us'

        # calling the method show_label and
        # having the output display the variable assignment
        # for each of the defined button instances with a label method value assignment
        about_button.show_label()
        contact_button.show_label()


class Button(object):
    def __init__(self):
        # Some important notes about self:
        # self refers to the class from which any instances might be created
        # methods of a class will have access to any attributes of that class
        # as long as they pass in the self parameter
        # this is default behavior so it should not be much of a concern
        # On the other hand, there is a difference between a variable defined within a class
        # and an attribute of a class.
        # with the self prefix you have an attribute that can be called by any method of the class
        # without the self prefix you simply have a variable and it's scope is limited to the class itself

        # calling the click() method from inside the Button() class
        # self.click()
        self.on_roll_over("Hello!")
        self.label = '' # public attribute - no underscores
        self.__size = 60 # private attribute - two underscores
        self._color = "xxxxxx" # protected attribute = one underscore

    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over the button" + message

    def show_label(self):
        print 'My label is ' + self.label


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
