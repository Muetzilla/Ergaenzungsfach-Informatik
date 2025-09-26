from datetime import datetime

class BankKonto:
    def __init__(self, konto_nummer, besitzer, currency="CHF", betrag=0.0):
        self.besitzer = besitzer
        self.konto_nummer = konto_nummer
        self.betrag = betrag
        self.currency = currency

    def __str__(self):
        return f"Kontonummer: {self.konto_nummer}, Besitzer: {self.besitzer}, Kontostand: {self.betrag:.2f} {self.currency}"

    def einzahlung(self, betrag):
        self.betrag += betrag

    def auszahlung(self, betrag):
        self.einzahlung(-betrag)


def ueberweisung(konto1, konto2, betrag):
    # Es wird die Währung von Konto 1 verwendet.
    konto1.auszahlung(betrag)
    konto2.einzahlung(betrag)

class Person:
    def __init__(self, vorname, nachname, geburtsdatum):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum

    def __str__(self):
      return f"{self.vorname} {self.nachname}, geboren am {self.geburtsdatum.day:02d}.{self.geburtsdatum.month:02d}.{self.geburtsdatum.year}"

    def alter(self):
        return (datetime.today() - self.geburtsdatum).days


