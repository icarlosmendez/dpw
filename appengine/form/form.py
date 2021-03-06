# form html content

class Form(object):
    def __init__(self):
        self.head = '''
        <!DOCTYPE HTML>
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Customer Survey</title>
        <meta name="Description" content="">
        <meta name="Keywords" content="Client Survey">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link href="css/normalize.css" rel="stylesheet" type="text/css">
        <link href="css/form.css" rel="stylesheet" type="text/css">
        <link href="css/jquery-ui.css" rel="stylesheet" type="text/css">
        <link href="css/jquery-ui.structure.css" rel="stylesheet" type="text/css">
        <link href="css/jquery-ui.theme.css" rel="stylesheet" type="text/css">

        <link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:300|Montserrat:700|Roboto+Slab' rel='stylesheet' type='text/css'>

        </head>
        <body>
        <div class="colorTabs"></div><!-- /colorTabs -->
            <div class="wrapper">

                <header>
                    <h1 class="hide-text">Carib</h1>
                    <div class="logoWrap">
                        <div class="logo"></div>
                    </div>
                </header>
                '''
        self.body = '''
                    <form class="formWrap" method="GET" action="">
                        <fieldset class="fieldWrap"><!-- Master Fieldset -->
                            <h3>Contact Information</h3>
                            <fieldset>
                                <div id="company" class="left">
                                <h4>Your Company</h4>
                                    <label>Company Name
                                        <input type="text" name="companyName" tabindex="1" placeholder="please enter your company name"/></label>
                                    <label>Current Or Desired URL
                                        <input type="text" name="url" placeholder="yourcompany.tld"/></label>
                                    <label>Anticipated Launch Date
                                        <input type="text" name="launchDate" id="datepicker" class="icon" placeholder="click here to enter a date"/></label>
                                    <label>How Cool Is Your Company
                                        <input type="range" name="quantity" min="1" max="10" /></label>
                                </div>
                                <div id="primary" class="left">
                                <h4>Primary Contact</h4>
                                    <label>Name
                                        <input type="text" name="priName" placeholder="firstname lastname"/></label>
                                    <label>Email
                                        <input type="email" name="priEmail" placeholder="you@yourcompany.tld"/></label>
                                    <label>Phone
                                        <input type="tel" name="priPhone" placeholder="(123)456-7890"/></label>
                                    <label>Company Role
                                        <select name="priRole">
                                            <option value="role">Choose One</option>
                                            <option value="role">Sole Proprietor</option>
                                            <option value="role">Partner</option>
                                            <option value="role">CEO</option>
                                            <option value="role">Producer</option>
                                            <option value="role">Project Manager</option>
                                            <option value="role">Creative Director</option>
                                        </select></label>
                                </div>
                                <div id="secondary" class="left">
                                <h4>Secondary Contact</h4>
                                    <label>Name
                                        <input type="text" name="secName" placeholder="firstname lastname"/></label>
                                    <label>Email
                                        <input type="email" name="secEmail" placeholder="you@yourcompany.tld"/></label>
                                    <label>Phone
                                        <input type="tel" name="secPhone" placeholder="(123)456-7890"/></label>
                                    <label>Company Role
                                        <select name="secRole">
                                            <option value="role">Choose One</option>
                                            <option value="role">Sole Proprietor</option>
                                            <option value="role">Partner</option>
                                            <option value="role">CEO</option>
                                            <option value="role">Producer</option>
                                            <option value="role">Project Manager</option>
                                            <option value="role">Creative Director</option>
                                        </select></label>
                                </div>
                            </fieldset>

                            <div id="submit">
                                <input class="right" type="submit" value="submit" />
                            </div>
                            '''
        self.close = '''
                        </fieldset><!-- /Master Fieldset -->
                    </form><!-- /formWrap -->
                </div><!-- /wrapper -->
            <footer>

            </footer>

        <!-- Java Script -->

            <!-- jQuery -->
            <script src="js/jquery-1.11.1.js"></script>
            <!-- required plugins -->
            <script src="js/jquery-ui-1.11.0.custom/jquery-ui.min.js"></script>
            <!-- other js -->
            <script src="js/form.js"></script>


        </body>
        </html>
        '''

    def print_out(self):
        html = self.head + self.body + self.close
        html = html.format(**locals())
        return html
