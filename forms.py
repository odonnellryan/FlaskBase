from wtforms import Form, StringField


class RegistrationForm(Form):

    def __init__(self, *args, **kwargs):
        self.email = self.email.lower()
        super(RegistrationForm,self).__init__(*args, **kwargs)

    name = StringField()
    email = StringField()