#
"""
Carlos Mendez
28MAR2015
DPW
Final Practical
"""
#

class Average():
    def __init__(self):
        pass

    def get_avg(self, grades):
        total = 0

        for i in grades:
            total += i

        average = total/len(grades)
        return average



class WebPage(object):
    def __init__(self):
        self.title =''
        self.css = "css/final.css"

        self.head = """
<!doctype HTML>
<html>
<head>
    <title>{self.title}</title>
    <link href="{self.css}" rel='stylesheet' />
</head>
</html>
    <body>
"""
        self.body = ''
        self.close = """
    </body>
</html>

"""

    def print_out(self):
        html = self.head + self.body + self.close
        html = html.format(**locals())
        return html