class Knoten:
    def __init__(self, inhalt, naechster):
        self.inhalt = inhalt
        self.naechster = naechster


    def __str__(self):
        return str(self.inhalt)


    def add_knoten(self, new_knoten):
        if self.naechster is None:
            self.naechster = new_knoten
        else:
            self.naechster.add_knoten(new_knoten)