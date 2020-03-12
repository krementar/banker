import unittest

import funcs
from banker import app


class Test(unittest.TestCase):

    def test_get_payments(self):
        with app.test_request_context('/payments',
                                      headers={"Authorization": "Test"}):
            result = funcs.get_payments()
            assert "data" in result
            assert result["data"] is not None

    def test_create_payment(self):
        with app.test_request_context('/payment/create',
                                      headers={"Authorization": "Test"},
                                      data={"amount": 10,
                                            "currency": 840,
                                            "description": "Test",
                                            "payer_email": "test@t.com"}):
            result = funcs.create_payment()
            assert "data" in result
            assert result["data"] is not None

    def test_get_payments_unauth(self):
        with app.test_request_context('/payments'):
            result = funcs.get_payments()
            assert "data" in result
            assert result["data"] is None


if __name__ == '__main__':
    unittest.main()
