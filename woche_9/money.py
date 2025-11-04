class Money:
    def __init__(self, amount,currency):

        self.amount = amount
        self.currency = currency

    def __str__(self):
      return f"{self.amount:.2f} {self.currency}"