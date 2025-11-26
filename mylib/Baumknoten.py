class Baumknoten:
    def __init__(self, key, name, daten, left_child, right_child, parent):
        self.key = key
        self.name = name
        self.daten = daten
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def __str__(self):
        return f"{self.name}: {self.daten}"