class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency.lower() == other.currency.lower():
            new_amount = self.amount + other.amount
            return Money(new_amount, self.currency)
        else:
            return f"Can't add {self.currency} & {other.currency}"

    def __str__(self):
        return f"{self.amount} {self.currency.upper()}"

    def __eq__(self, other):
        if isinstance(other, Money):
            if self.currency == other.currency:
                return True
            else:
                return False


user1 = Money(1200,"usd")
user2 = Money(300,"usd")

print(user1==user2)

combine_amount = user1 + user2
print(combine_amount)

