from mylib.Knoten import Knoten

class Liste:
    def __init__(self, anker=None):
        self.anker = anker

    def __str__(self):
        return ", ".join(str(k.inhalt) for k in self.iter_knoten())

    def iter_knoten(self):
        current = self.anker
        while current is not None:
            yield current
            current = current.naechster

    def __iter__(self):
        for knoten in self.iter_knoten():
            yield knoten.inhalt


    def vorherige_setzen(self):
        prev = None
        current = self.anker
        while current is not None:
            current.vorheriger = prev
            prev = current
            current = current.naechster

    def finde_letzten(self):
        current = self.anker
        if current is None:
            return None
        while current.naechster is not None:
            current = current.naechster
        return current

    def add_knoten(self, new_knoten):
        if self.anker is None:
            self.anker = new_knoten
            return
        last = self.finde_letzten()
        last.naechster = new_knoten
        new_knoten.vorheriger = last

    def append(self, inhalt):
        self.add_knoten(Knoten(inhalt))

    def suchen(self, inhalt):
        current = self.anker
        while current is not None:
            if current.inhalt == inhalt:
                return current
            current = current.naechster
        return None

    def entfernen(self, inhalt):
        current = self.anker
        while current is not None:
            if current.inhalt == inhalt:
                if current.vorheriger is not None:
                    current.vorheriger.naechster = current.naechster
                else:
                    self.anker = current.naechster
                if current.naechster is not None:
                    current.naechster.vorheriger = current.vorheriger
                return True
            current = current.naechster
        return False

    def einfuegen(self, neuer_knoten):
        if self.anker is None:
            self.anker = neuer_knoten
            return

        if neuer_knoten.inhalt <= self.anker.inhalt:
            neuer_knoten.naechster = self.anker
            self.anker.vorheriger = neuer_knoten
            self.anker = neuer_knoten
            return

        prev = self.anker
        current = self.anker.naechster
        while current is not None and current.inhalt < neuer_knoten.inhalt:
            prev, current = current, current.naechster

        neuer_knoten.naechster = current
        neuer_knoten.vorheriger = prev
        prev.naechster = neuer_knoten
        if current is not None:
            current.vorheriger = neuer_knoten