from wtforms import Form, StringField


class RegistrationForm(Form):

    def __init__(self, *args, **kwargs):
        if hasattr(self.email, 'data'):
            self.email.data = self.email.data.lower()
        super(RegistrationForm, self).__init__(*args, **kwargs)

    name = StringField()
    email = StringField()