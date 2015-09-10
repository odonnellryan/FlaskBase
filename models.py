from peewee import SqliteDatabase, CharField, Model

db = SqliteDatabase('test.db')

class BaseModel(Model):
    class Meta:
        database = db # This model uses the "people.db" database.

class Person(Model):
    name = CharField()

