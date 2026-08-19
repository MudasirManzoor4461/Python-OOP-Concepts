class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def process_payment(self):
         pass

class CreditCardPayment(Payment):
    def __init__(self, amount, currency, card_holder_name, card_number):
        super().__init__(amount, currency)
        self.card_holder_name = card_holder_name
        self.card_number = card_number

    def process_payment(self):
        print(f"Dear {self.card_holder_name} You credited amount {self.amount}{self.currency.upper()} Card Number {self.card_number}")
        

class BankTransferPayment(Payment):
    def __init__(self, amount, currency, bank_name):
        super().__init__(amount, currency)
        self.bank_name = bank_name

    def process_payment(self):
        print(f"Processing bank transfer of {self.currency} {self.amount} via {self.bank_name}... Transferred successfully!")

class CashPayment(Payment):
        def __init__(self, amount, currency, reciept_no):
            super().__init__(amount, currency)
            self.reciept_no = reciept_no

        def process_payment(self):
            print(f"Processing cash payment of {self.currency} {self.amount} at counter. Receipt #{self.reciept_no} generated successfully!")


def trigger_payment(payment_obj):
    payment_obj.process_payment()


card_payment = CreditCardPayment(500, "pkr","Mudasir",1234)
bank_payment = BankTransferPayment(1200,"pkr","HBL")
cash_payment = CashPayment(1200,"pkr",1234)

payments = [card_payment, bank_payment, cash_payment]

for items in payments:
    trigger_payment(items)
