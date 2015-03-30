# response html content

class Output(object):
    def __init__(self):
        self.reply = '''
            <fieldset class="fieldWrap"><!-- Master Fieldset -->
                <h3>Contact Information</h3>
                <fieldset>
                    <div id="company" class="left">
                        <h4>Your Company</h4>
                            <label>Company Name
                                <h5>{companyName}</h5></label>
                            <label>Current Or Desired URL
                                <h5>{url}</h5></label>
                            <label>Anticipated Launch Date
                                <h5>{launchDate}</h5></label>

                    </div>
                </fieldset>
            </fieldset>
        '''

        self.reply = self.reply.format(**locals())


    def print_out(self):
        html = form.head + self.body + form.close
        html = html.format(**locals())
        return html
