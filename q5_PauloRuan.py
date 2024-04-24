import sys


def decrypt():
    message = 'GIEWIVrGMTLIVrHIQS'  # encrypted message
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
            if num < 0:
                num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        return translated


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result


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
    return check_credentials(transaction, {"bank": input("please insert bank name: "), "id": input("please insert cpf"), "password": encrypt(input("please insert password"), 4)}, input("Confirm?\n[Y]es\n[N]o\n"))


def confirm_trans_credit(transaction):
    return check_credentials(transaction, {"card": input("please insert card flag: "), "password": encrypt(input("please insert password"), 4)}, input("Confirm?\n[Y]es\n[N]o\n"))


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
