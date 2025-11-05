class Liste:
    def __init__(self, anker):
        self.anker = anker


    def __str__(self):
        wholeList = str(self.anker.inhalt) + ", "
        next_element = self.anker.naechster
        while next_element.naechster is not None:
            wholeList += str(next_element.inhalt) + ", "
            next_element = next_element.naechster
        wholeList += str(next_element.inhalt)
        return wholeList

    def add_element(self, new_knoten):
        next_element = self.anker.naechster
        while next_element.naechster is not None:
            next_element = next_element.naechster
        next_element.naechster = new_knoten

    def add_element_via_knoten(self, new_knoten):
       self.anker.add_knoten(new_knoten)

    def findeLetzten(self):
        next_element = self.anker.naechster
        while next_element.naechster is not None:
            next_element = next_element.naechster
        return next_element

    def suchen(self, inhalt):
        if self.anker.inhalt is inhalt:
            return self.anker
        next_element = self.anker.naechster
        while next_element.naechster is not None:
            if next_element.inhalt is inhalt:
                return inhalt
            next_element = next_element.naechster
        return None

    def entfernen(self, inhalt):
        if self.anker.inhalt is inhalt:
            self.anker = self.anker.naechster
        else:
            next_element = self.anker.naechster
            old_element = self.anker
            while next_element.naechster is not None:
                if next_element.inhalt is inhalt:
                    old_element.naechster = next_element.naechster
                    break
                else:
                    old_element = next_element
                    next_element = next_element.naechster

    def einfuegen(self, neuer_knoten):
        if neuer_knoten.inhalt < self.anker.inhalt:
            tmp = self.anker
            self.anker = neuer_knoten
            self.anker.naechster = tmp
        else:
            next_element = self.anker.naechster
            old_element = self.anker
            print("Hinzuzufügender Knoten: ", neuer_knoten.inhalt)
            while next_element.naechster is not None:
                if old_element.inhalt <= neuer_knoten.inhalt <= next_element.inhalt:
                    print("hinzufügen zwischen: ", old_element, " und ", next_element)
                    old_element.naechster = neuer_knoten
                    neuer_knoten.naechster = next_element
                    print("neue folge: ", old_element,"->", neuer_knoten, "->", next_element)
                old_element = next_element
                next_element = next_element.naechster
                print("Nun: ", old_element, "->", next_element)
            if next_element.inhalt >= neuer_knoten.inhalt:
                old_element.naechster = neuer_knoten
                neuer_knoten.naechster = next_element
            else:
                next_element.naechster = neuer_knoten
                neuer_knoten.naechster = None
