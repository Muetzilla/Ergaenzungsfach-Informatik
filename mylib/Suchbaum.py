from graphviz import Digraph

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


    # def plot(self):
    #     plot = Digraph(format="png", graph_attr={"root": str(self.anker.key)})
    #
    #     def add_edges(node):
    #         if node.left_child is not None:
    #             plot.edge(str(node.key), str(node.left_child.key), color="red")
    #             add_edges(node.left_child)
    #         if node.right_child is not None:
    #             plot.edge(str(node.key), str(node.right_child.key), color="green")
    #             add_edges(node.right_child)
    #
    #     add_edges(self.anker)
    #     plot.render(cleanup=True, filename="suchbaum_plot")
    def plot(self):
        dot = Digraph()
        dot.node(str(self.anker.key))

        def add_nodes_edges(node):
            if node.left_child is not None:
                dot.node(str(node.left_child.key))
                dot.edge(str(node.key), str(node.left_child.key))
                add_nodes_edges(node.left_child)
            if node.right_child is not None:
                dot.node(str(node.right_child.key))
                dot.edge(str(node.key), str(node.right_child.key))
                add_nodes_edges(node.right_child)

        add_nodes_edges(self.anker)
        dot.render('binary_tree', view=True, format='png')

