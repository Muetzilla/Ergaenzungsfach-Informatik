

class Knoten:
    def __init__(self, inhalt = 0, naechster = None):
        self.naechster = naechster
        self.inhalt = inhalt
    def __str__(self):
        return str(self.inhalt)

class Liste:
    class Iterator:
        def __init__(self, liste):
            self.currentNode = liste.anker
            self.liste = liste

        def __next__(self):
            if self.currentNode is None:
                raise StopIteration
            else:
                tempValue = self.currentNode
                self.currentNode = self.currentNode.naechster
                return tempValue

    def __init__(self, anker = None):
        self.anker = anker

    def __str__(self):
      anzeige = "–"
      knoten = self.anker
      while knoten != None:
          anzeige = anzeige + str(knoten.inhalt) + "–"
          knoten = knoten.naechster
      return anzeige

    def __iter__(self):
        return Liste.Iterator(self)


    def findeLetzten(self):
        if self.anker == None:
            return None
        knoten = self.anker
        while knoten.naechster != None:
            knoten = knoten.naechster
        return knoten

    def append(self, inhalt):
        aktuellletzter = self.findeLetzten()
        knoten = Knoten(inhalt)
        if aktuellletzter == None:
            self.anker = knoten
        else:
            aktuellletzter.naechster = knoten



