from datetime import datetime
from mylib.banking import BankKonto, Person, ueberweisung

max= Person("Max", "Mustermann", geburtsdatum = datetime(2001, 5, 12))
maurice = Person("Maurice", "Meier", geburtsdatum = datetime(2004, 3, 15))
franz = Person("Franz", "Schneider", geburtsdatum = datetime(2007, 9, 19))

konto1 = BankKonto("1234", max, betrag=1000.0)
konto2 = BankKonto("4321", maurice, betrag=2000.0)
konto3 = BankKonto("1357", franz, betrag=3000.0)
konto4 = BankKonto("1122", max, betrag=7000.0)
konto5 = BankKonto("9926", maurice, betrag=30000.0)

print(konto1)
print(konto2)
print(konto3)
print(konto4)
print(konto5)


print(konto1)
print("\n--------------------------------------")
konto1.einzahlung(10000)
print(konto1)
print("--------------------------------------")
konto1.auszahlung(2000)
print(konto1)

print("\n--------------------------------------")

print(konto1)
print(konto2)
ueberweisung(konto1, konto2, 5000)
print(konto1)
print(konto2)
print("\n--------------------------------------")

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
    eingabe = input("Was möchten Sie tun? (e)einzahlen, (a)auszahlen, (t)überweisung, (x)beenden (s)alle anzeigen (n)neuer Kunde (k) neues Konto anlegen > ")
    if eingabe == "x":
        break
    elif eingabe == "e":
        kontonummer = input("Kontonummer > ")
        konto = konten[kontonummer]
        if konto is None:
            print("Konto nicht gefunden!")
            continue
        betrag = float(input("Betrag > "))
        konto.einzahlung(betrag)
        print(konto)
    elif eingabe == "a":
        kontonummer = input("Kontonummer > ")
        konto = konten[kontonummer]
        if konto is None:
            print("Konto nicht gefunden!")
            continue
        betrag = float(input("Betrag > "))
        konto.auszahlung(betrag)
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
        betrag = float(input("Betrag > "))
        ueberweisung(konto_von, konto_nach, betrag)
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
