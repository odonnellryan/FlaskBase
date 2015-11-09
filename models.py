from peewee import SqliteDatabase, CharField, Model

db = SqliteDatabase('test.db')

class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.

class Person(Model):

    name = CharField()
    email = CharField()
    password = CharField()
    authenticated = CharField()

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Person, self).save(*args, **kwargs)
