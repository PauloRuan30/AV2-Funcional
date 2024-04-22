import unittest
from q1_GustavoTakeda import *


class TestPaymentActions(unittest.TestCase):
    def test_cash(self):
        x = processar(cash_payment, bank_deposit,
                      credit_payment, create_transaction(a))
        self.assertEquals(type(x), String, "Should be string")

    def test_bank(self):
        x = processar(cash_payment, bank_deposit,
                      credit_payment, create_transaction(a))
        self.assertEquals(x, {"costumer": "Gustavo", "type": "bank_deposit",
                          "bank": "Bradesco", "status": "confirmed"})

    def test_credit():
        x = processar(cash_payment, bank_deposit,
                      credit_payment, create_transaction(a))
        self.assertEquals(x, {"costumer": "Gustavo", "type": "credit",
                          "card": "Mastercard", "status": "confirmed"})


if __name__ == "__main__":
    unittest.main()
