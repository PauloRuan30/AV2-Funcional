import sys


def a(b): return b if b == 1 or b == 2 or b == 3 or b == 4 else a(b())


def c(): return int(
    input("Please select a type of transaction or exit:\n[1]Cash \n[2]Fund Transfer\n[3]Credit\n[4]Exit\n"))


def create_transaction(a):
    return {
        "costumer": input("Name of the costumer: "),
        "value": float(input("value: R$")),
        "type": a(c)}


def cash_payment(client_payment):
    print(
        f"value: R$ {client_payment['value']}\nstatus: paid")
    return confirm_trans_cash(client_payment)


def credit_payment(client_payment):
    return confirm_trans_credit(client_payment)


def bank_deposit(client_payment):
    return confirm_trans_bank(client_payment)


def processar(cash, bank, credit, transaction_type):
    if transaction_type["type"] == 1:
        return cash(transaction_type)
    if transaction_type["type"] == 2:
        return bank(transaction_type)
    if transaction_type["type"] == 3:
        return credit(transaction_type)
    if transaction_type["type"] == 4:
        print("Terminating operations\nHave a good day! :3")
        sys.exit()


def confirm_trans_cash(transaction):
    return f"COSTUMER: {transaction['costumer']}\nSTATUS: DONE\n "


def confirm_trans_bank(transaction):
    return check_credentials(transaction, {"bank": input("please insert bank name: "), "id": input("please insert cpf"), "password": input("please insert password")}, input("Confirm?\n[Y]es\n[N]o\n"))


def confirm_trans_credit(transaction):
    return check_credentials(transaction, {"card": input("please insert card flag: "), "password": input("please insert password")}, input("Confirm?\n[Y]es\n[N]o\n"))


def check_credentials(transaction, credentials, wanna_exit):
    if wanna_exit == "Y" or "y":
        print("Terminating operations\nHave a good day! :3")
        sys.exit()
    if transaction["type"] == 2:
        return {"costumer": transaction["costumer"],
                "type": "bank transfer",
                "bank": credentials["bank"],
                "status": "confirmed"
                }
    if transaction["type"] == 3:
        return {"costumer": transaction["costumer"],
                "type": "credit",
                "card": credentials["card"],
                "status": "confirmed"
                }


# print(create_transaction(a))
print("Welcome to the payment processor!")
print(processar(cash_payment, bank_deposit, credit_payment, create_transaction(a)))
