from peewee import (Model, SqliteDatabase, DoubleField, CharField, IntegerField, DateTimeField,
                    datetime as peewee_datetime)
from config import DB_NAME


payments_db = SqliteDatabase(DB_NAME)


class Payment(Model):
    class Meta:
        db = payments_db

    amount = DoubleField()
    currency = IntegerField()
    created = DateTimeField(default=peewee_datetime.datetime.now)
    description = CharField(max_length=100)
    payer_email = CharField(max_length=100)

    def to_dict(self):
        return self._data


Payment.create_table(True)
