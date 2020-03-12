from flask import Flask, request
from peewee import (Model, SqliteDatabase, DoubleField, CharField, IntegerField, DateTimeField,
                    datetime as peewee_datetime)


app = Flask(__name__)

payments_db = SqliteDatabase("payments.db")


class Payment(Model):
    class Meta:
        db = payments_db

    amount = DoubleField()
    currency = IntegerField()
    created = DateTimeField(default=peewee_datetime.datetime.now)
    description = CharField(max_length=100)
    payer_email = CharField(max_length=100)


@app.route("/import", methods=["POST"])
def import_payments():
    if "Authorization" not in request.headers:
        return {"data": None, "error": "Invalid request"}
    return {"data": "Importing payments ...", "error": "Ok"}


@app.route("/payments", methods=["GET"])
def get_payments():
    if "Authorization" not in request.headers:
        # abort(403)
        return {"data": None, "error": "Invalid request"}
    return {"data": "Getting payments ...", "error": "Ok"}


@app.route("/payment/create", methods=["POST"])
def create_payment():
    if "Authorization" not in request.headers:
        # abort(403)
        return {"data": None, "error": "Invalid request"}
    return {"data": "Creating payments ...", "error": "Ok"}


app.run()
