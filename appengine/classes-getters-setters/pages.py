
class Page(object):
    def __init__(self):
        self.__title = ''
        self.__css = ''
        self.head = """
<!doctype HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """
        self.body = "Some kinda buhloney"
        self.close = """
    </body>
</html>
        """

    # def print_out(self):
    #     all = self.head + self.body + self.close
    #     all = all.format(**locals())
    #     return all

        # The attribute .whole_page and the update() method
        # is taking the place of the print_out() method above
        # which has been commented out but left in place
        self.whole_page = ''

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())
        return self.whole_page

    # We have a getter/setter pair for the title variable of the web page
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title
        self.update()


    # We have a getter/setter pair for the body variable of the web page
    # @property
    # def body(self):
    #     return self.__body
    #
    # @body.setter
    # def body(self, new_body):
    #     self.__body = new_body
    #     self.update()


    # We have a getter/setter pair for the css variable of the web page
    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file
        self.update()


