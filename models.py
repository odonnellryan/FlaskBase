from peewee import SqliteDatabase, CharField, Model
db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class Person(Model):
    name = CharField()
    email = CharField()

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(Person, self).save(*args, **kwargs)

