class Knoten:
    def __init__(self, inhalt, naechster):
        self.inhalt = inhalt
        self.naechster = naechster


    def __str__(self):
        return str(self.inhalt)