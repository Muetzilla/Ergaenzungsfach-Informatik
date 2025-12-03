from graphviz import Digraph

from mylib.Baumknoten import Baumknoten


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

    def insertNode(self, node):
        current = self.anker
        parent = None
        isInsertionDone = False
        if self.anker is None:
            self.anker = node
            isInsertionDone = True
        while not isInsertionDone:
            parent = current
            if node.key == current.key:
                raise KeyError("Schlüssel bereits vorhanden, bitte nur eindeutige Schlüssel verwenden.")
            elif node.key < current.key:
                if current.left_child is None:
                    isInsertionDone = True
                else:
                    current = current.left_child
            else:
                if current.right_child is None:
                    isInsertionDone = True
                else:
                    current = current.right_child
        node.parent = parent
        if node.key < parent.key:
            parent.left_child = node
        else:
            parent.right_child = node

    def insert(self, schluessel, name, daten):
        neuer_knoten = Baumknoten(schluessel, name, daten, None, None, None)
        if self.anker is None:
            self.anker = neuer_knoten
        else:
            self.insertNode(neuer_knoten)


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

    def delete(self, knoten):
        def is_leaf(node):
            return node.left_child is None and node.right_child is None
        if is_leaf(knoten):
            if knoten.parent.left_child == knoten:
                knoten.parent.left_child = None
            else:
                knoten.parent.right_child = None

    def __str__(self):
        anzeige = "-"
        if self.anker is not None:
            anzeige += str(self.anker.key)
            anzeige += "-"

        def add(node):
            nonlocal anzeige
            if node.left_child is not None:
                anzeige += str(node.left_child.key)
                anzeige += "-"
                add(node.left_child)
            if node.right_child is not None:
                anzeige += str(node.right_child.key)
                anzeige += "-"
                add(node.right_child)

        add(self.anker)
        return anzeige

    def inorder_traversal(self, node, result):
        if node is not None:
            self.inorder_traversal(node.left_child, result)
            result.append(node.key)
            self.inorder_traversal(node.right_child, result)
        return result

    def preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.key)
            self.preorder_traversal(node.left_child, result)
            self.preorder_traversal(node.right_child, result)
        return result

    def postorder_traversal(self, node, result):
        if node is not None:
            self.postorder_traversal(node.left_child, result)
            self.postorder_traversal(node.right_child, result)
            result.append(node.key)

        return result

    def plot(self):
        dot = Digraph()
        dot.node(str(self.anker.key))

        def add_nodes_edges(node):
            if node.left_child is not None:
                dot.node(str(node.left_child.key))
                dot.edge(str(node.key), str(node.left_child.key), color="red")
                add_nodes_edges(node.left_child)
            if node.right_child is not None:
                dot.node(str(node.right_child.key))
                dot.edge(str(node.key), str(node.right_child.key), color="green")
                add_nodes_edges(node.right_child)

        add_nodes_edges(self.anker)
        dot.render('binary_tree', view=True, format='png')

    def guete(self):
        if self.anker is None:
            return 0
        guete_sum = 0
        guete_number_of_nodes = 0
        def depth(node, guete_depth):
            nonlocal guete_sum, guete_number_of_nodes
            if node is not None:
                depth(node.left_child, guete_depth + 1)
                depth(node.right_child, guete_depth + 1)
                guete_sum += guete_depth + 1
                guete_number_of_nodes += 1

        depth(self.anker, 0)
        print("Summe der Tiefen:", guete_sum)
        print("Anzahl der Knoten:", guete_number_of_nodes)
        if guete_number_of_nodes > 0:
            return guete_sum / guete_number_of_nodes
        else:
            return 0