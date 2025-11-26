class Suchbaum:
    def __init__(self, anker):
        self.anker = anker

    def suchen(self, wert):
        current = self.anker
        while current is not None:
            if wert == current.key:
                return current
            elif wert < current.key:
                current = current.left_child
            else:
                current = current.right_child
        return None

    def einfuegen(self, neuer_knoten):
        current = self.anker
        parent = None
        while current is not None:
            if neuer_knoten.key == current.key:
                pass
            elif neuer_knoten.key < current.key:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        if parent.key < neuer_knoten.key:
            parent.right_child = neuer_knoten
        else:
            parent.left_child = neuer_knoten
        neuer_knoten.parent = parent

    def __str__(self):
        def traverse(node, depth):
            if node is None:
                return ""
            indent = "-" * depth
            result = f"{indent}{node.name}\n"
            result += traverse(node.left_child, depth + 1)
            result += traverse(node.right_child, depth + 1)
            return result

        return traverse(self.anker, 0)

