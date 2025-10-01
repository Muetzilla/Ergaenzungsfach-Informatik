from datetime import datetime
from mylib.banking import BankKonto, Person, ueberweisung, convert
from woche_8.yahoo_api import yahoo_fx_rate

max= Person("Max", "Mustermann", geburtsdatum = datetime(2001, 5, 12))
maurice = Person("Maurice", "Meier", geburtsdatum = datetime(2004, 3, 15))
franz = Person("Franz", "Schneider", geburtsdatum = datetime(2007, 9, 19))

konto1 = BankKonto("1", max, betrag=1000.0)
konto2 = BankKonto("2", maurice, betrag=2000.0)
konto3 = BankKonto("3", franz, betrag=3000.0)
konto4 = BankKonto("4", max, currency="AUD",betrag=7000.0)
konto5 = BankKonto("5", maurice, currency="EUR", betrag=30000.0)
verfuegbare_waehrungen = ["USD", "NOK", "EUR", "GBP", "JPY", "CAD", "AUD"]

wechselkurse = {}
for waehrung in verfuegbare_waehrungen:
    wechselkurse[waehrung] =  yahoo_fx_rate(waehrung, "CHF")
# wechselkurse = {"USD": 0.79, "BAM": 0.48, "NOK": 0.08, "EUR":0.93,"GBP":0.93, "CHF":1., "JPY": 0.0054, "CAD": 0.57, "AUD": 0.52} # Wie viele CHF pro Währung

def print_wechselkurse():
    for waehrung, kurs in wechselkurse.items():
        print(f"1 {waehrung} = {kurs} CHF")


# print(konto1)
# print(konto2)
# print(konto3)
# print(konto4)
# print(konto5)
#
#
# print(konto1)
# print("\n--------------------------------------")
# konto1.einzahlung(10000)
# print(konto1)
# print("--------------------------------------")
# konto1.auszahlung(2000)
# print(konto1)

# print("\n--------------------------------------")
#
# print(konto1)
# print(konto2)
# # ueberweisung(konto1, konto2, 5000)
# print(konto1)
# print(konto2)
# print("\n--------------------------------------")

print(konto1)
print(konto2)
print(konto3)
print(konto4)
print(konto5)
print("\n")
# "Datenbank" unserer Konten
konten = {}
for konto in [konto1, konto2, konto3, konto4, konto5]:
    konten[konto.konto_nummer] = konto

# "Dankebank" unserer Kunden
personen = [max, maurice, franz]

while True:
    eingabe = input("Was möchten Sie tun? (e)einzahlen, (a)auszahlen, (t)überweisung, (x)beenden (s)alle anzeigen (n)neuer Kunde (k) neues Konto anlegen (w)Währungen anzeigen (c)change > ")
    if eingabe == "x":
        print("Exit")
        break
    elif eingabe == "e":
        kontonummer = input("Kontonummer > ")
        konto = konten[kontonummer]
        if konto is None:
            print("Konto nicht gefunden!")
            continue
        betrag = float(input("Betrag > "))
        waehrung = input(f"In welcher Währung soll überwiesen werden?({wechselkurse.keys()}) > ")
        konto.einzahlung(convert(betrag, waehrung, konto.currency, wechselkurse))
        print(konto)
    elif eingabe == "a":
        kontonummer = input("Kontonummer > ")
        konto = konten[kontonummer]
        if konto is None:
            print("Konto nicht gefunden!")
            continue
        print(f"Aktueller Kontostand: {konto.betrag} {konto.currency}")
        betrag = float(input("Betrag > "))
        waehrung = input(f"In welcher Währung soll überwiesen werden?({wechselkurse.keys()}) > ")
        konto.auszahlung(convert(betrag, waehrung, konto.currency, wechselkurse))
        print(konto)
    elif eingabe == "t":
        kontonummer = input("1. Kontonummer > ")
        konto_von = konten[kontonummer]
        if konto is None:
            print("Konto nicht gefunden!")
            continue
        kontonummer = input("2. Kontonummer > ")
        konto_nach = konten[kontonummer]
        if konto is None:
            print("Konto nicht gefunden!")
            continue
        print(f"Aktueller Kontostand: {konto_von.betrag} {konto.currency}")
        betrag = float(input("Betrag > "))
        if konto_von.currency != konto_nach.currency:
            waehrung = input(f"In welcher Währung soll überwiesen werden?({konto_von.currency}, {konto_nach.currency}) > ")
            ueberweisung(konto_von, konto_nach, betrag, waehrung, wechselkurse)
        else:
            ueberweisung(konto_von, konto_nach, betrag, konto_von.currency, wechselkurse)
        print(konto_von)
        print(konto_nach)
    elif eingabe == "s":
        for konto in konten.values():
            print(konto)
    elif eingabe == "n":
        vorname = input("Vorname > ")
        nachname = input("Nachname > ")
        tag = int(input("Geburtstag (Tag) > "))
        monat = int(input("Geburtstag (Monat) > "))
        jahr = int(input("Geburtstag (Jahr) > "))
        geburtsdatum = datetime(jahr, monat, tag)
        person = Person(vorname, nachname, geburtsdatum)
        personen.append(person)
        print(f"Neuer Kunde angelegt: {person}")
    elif eingabe == "k":
        kontonummer = input("Kontonummer > ")
        besitzer_name = input("Besitzer (Vorname Nachname) > ")
        besitzer = None
        for person in personen:
            if f"{person.vorname} {person.nachname}" == besitzer_name:
                besitzer = person
                break
        if besitzer is None:
            print("Kunde nicht gefunden!")
            continue
        betrag = float(input("Anfangsbetrag > "))
        konto = BankKonto(kontonummer, besitzer, betrag=betrag)
        konten[kontonummer] = konto
        print(f"Neues Konto angelegt: {konto}")
    elif eingabe == "w":
        print("Wechselkurse (pro 1 CHF):")
        print_wechselkurse()
    elif eingabe == "c":
        print("Wechselkurse (pro 1 CHF):")
        print_wechselkurse()
        betrag = float(input("Wechselbetrag > "))
        waehrung_from = input(f"Von welcher Währung?({wechselkurse.keys()}) > ")
        waehrung_to = input(f"In welche Währung?({wechselkurse.keys()}) > ")
        converted = convert(betrag, waehrung_from, waehrung_to, wechselkurse)
        print(f"{betrag} {waehrung_from} = {converted:.2f} {waehrung_to}")





