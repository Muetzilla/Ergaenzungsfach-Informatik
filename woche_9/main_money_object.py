# from money import Money
from mylib.banking import convert
class Money:

    currencies = ["CHF", "EUR", "USD"]
    wechselkurse = {"CHF" : 1.0, "EUR": 0.95, "USD": 0.85}

    def __init__(self, amount,currency):
        assert currency in self.currencies, f"{currency}  is not a valid currency"
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __add__(self, other):
        currency = self.currency
        amount = self.amount + convert(other.amount, other.currency, currency, self.wechselkurse)
        return Money(amount, currency)

    def __sub__(self, other):
        currency = self.currency
        amount = self.amount - convert(other.amount, other.currency, currency, self.wechselkurse)
        return Money(amount, currency)

    def __mul__(self, other):
        return Money(self.amount * other, self.currency)

    def to_currency(self, currency):
        return Money(convert(self.amount, self.currency, currency, self.wechselkurse), currency)


#Main
print("Aktuelle Wechselkurse: " , Money.wechselkurse)

lohn = Money(150000, "CHF")
bonus = Money (30000, "EUR")

print("Lohn:", lohn)
print("Bonus:", bonus)

verguetung = lohn + bonus
print("Vergütung:", verguetung)

steuer = Money(verguetung.amount * 0.12, "USD")
netto = verguetung - steuer
print("Was übrig bleibt:", netto)

print("Was übrig bleibt in USD:", Money(0, "USD") + netto)
print("Was übrig bleibt in USD:", netto.to_currency("USD"))
print("Was übrig bleibt in USD:", netto + Money(0, "USD") )
print("Was übrig bleibt in EUR:", netto.to_currency("EUR"))

total = (verguetung + bonus - steuer).to_currency("EUR")
print("Total:", total)

print("\nZinseszinsrechnung:")
print("Anfangskapital:", netto)
anfangskapital = netto
zins = 1.05
for i in range(10):
    netto = netto * zins
    print(f"Jährlich mit Zins: {netto}, durch Zins erwirtschaftet: {netto - anfangskapital}")
print(f"Nach 10 Jahren mit Zins: {netto}, davon durch Zins erwirtschaftet: {netto - anfangskapital}")