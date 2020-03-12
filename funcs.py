import logging

from flask import request

from models import Payment


logger = logging.getLogger('banker')


def check_auth():
    if "Authorization" not in request.headers:
        raise Exception("Invalid request")


def import_payments():
    try:
        logger.debug("import_payments started")
        check_auth()
        return {"data": "Importing payments ...", "error": "Ok"}
    except Exception as ex:
        logger.warning(ex)
        return {"data": None, "error": str(ex)}
    finally:
        logger.debug("import_payments finished")


def get_payments():
    try:
        logger.debug("get_payments started")
        check_auth()
        # TODO add filters
        payments = Payment.select()
        return {"data": [p.to_dict() for p in payments], "error": "Ok"}
    except Exception as ex:
        logger.warning(ex)
        return {"data": None, "error": str(ex)}
    finally:
        logger.debug("get_payments finished")


def create_payment():
    try:
        logger.debug("create_payment started")
        check_auth()
        # TODO add check form params
        payment = Payment.create(**request.form)
        return {"data": payment.to_dict(), "error": "Ok"}
    except Exception as ex:
        logger.warning(ex)
        return {"data": None, "error": str(ex)}
    finally:
        logger.debug("create_payment finished")
