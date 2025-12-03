class Knoten():
    def __init__(self, inhalt=0, naechster=None):
        self.inhalt = inhalt
        self.naechster = naechster


class Liste():
    def __init__(self, anker=None):
        self.anker = anker

    def __str__(self):
        anzeige = "["
        separator = ", "
        knoten = self.anker
        while knoten is not None:
            anzeige = anzeige + str(knoten.inhalt)
            knoten = knoten.naechster
            if knoten is not None:
                anzeige = anzeige + separator
        return anzeige + "]"

    def finde_letzten(self):
        if self.anker is None:
            return None
        knoten = self.anker
        while knoten.naechster is not None:
            knoten = knoten.naechster
        return knoten

    def anhaengen(self, inhalt):
        knoten = Knoten(inhalt=inhalt)
        letzter = self.finde_letzten()
        if letzter is None:
            self.anker = knoten
        else:
            letzter.naechster = knoten

    def __len__(self):
        """
        Gibt die Anzahl Elemente in der Liste zurück
        """
        count = 0
        current_knoten = self.anker
        while current_knoten is not None:
            current_knoten = current_knoten.naechster
            count += 1
        return count


    def finde_knoten(self, index):
        """
        Gibt den Knoten mit dem Index `index` zurück
        """
        if index < 0 or index >= len(self):
            return None
        count = 0
        current_knoten = self.anker
        while current_knoten is not None:
            if count == index:
                return current_knoten
            current_knoten = current_knoten.naechster
            count += 1
        return None

    def __getitem__(self, index):
        """
        Adressoperator: Gibt Inhalt an der Position mit Index `index` zurück.
        Beispiel:
        a = liste[3]
        """
        raise NotImplementedError

    def __setitem__(self, index, inhalt):
        """
        Adressoperator: Überschreibt den Wert an Position mit Index `index` mit neuem Wert `inhalt`
        """
        raise NotImplementedError

    def einfuegen(self, index, inhalt):
        """
        Fügt Inhalt `inhalt` an Position mit Index `index` ein.
        """
        raise NotImplementedError

    def __iter__(self):
        """
        Erlaubt Verwendung als Iterable: Beispiel

        for inhalt in list:
            print(inhalt)
        """
        raise NotImplementedError
