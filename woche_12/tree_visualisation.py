import matplotlib.pyplot as plt

data = """
- Amycus: 2002 GB10
-- Bienor: 2000 QC243
-- Echeclus: 2000 EC98
- Sedna: 2003 VB12
-- Crantor: 2002 GO9
-- Eris: 2003 UB313
"""

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def parse_tree(text):
    lines = [line for line in text.splitlines() if line.strip()]
    root = None
    stack = []

    for line in lines:
        stripped = line.lstrip('-')
        depth = len(line) - len(stripped)
        name = stripped.strip()

        node = Node(name)

        if depth == 0:
            root = node
            stack = [node]
        else:
            # Elternknoten ist der letzte Knoten auf Level depth-1
            parent = stack[depth - 1]
            parent.children.append(node)

            # Stack aktualisieren
            if len(stack) > depth:
                stack[depth] = node
                stack = stack[:depth + 1]
            else:
                stack.append(node)

    return root

# --- SCHÖNE ZENTRIERUNG: Breitester Unterbaum bestimmt die x-Position ---
def compute_subtree_widths(node):
    if not node.children:
        return 1
    return sum(compute_subtree_widths(child) for child in node.children)

def assign_positions(node, x_offset, depth, positions):
    width = compute_subtree_widths(node)

    # Startposition des ersten Kindes
    child_x = x_offset

    positions[node] = (x_offset + width / 2, -depth)

    for child in node.children:
        child_width = compute_subtree_widths(child)
        assign_positions(child, child_x, depth + 1, positions)
        child_x += child_width


def plot_tree(root):
    positions = {}
    assign_positions(root, 0, 0, positions)

    fig, ax = plt.subplots(figsize=(10, 6))

    # Kanten zeichnen
    def draw_edges(node):
        x0, y0 = positions[node]
        for child in node.children:
            x1, y1 = positions[child]
            ax.plot([x0, x1], [y0, y1])
            draw_edges(child)

    draw_edges(root)

    # Knoten + Labels zeichnen (Label RECHTS)
    for node, (x, y) in positions.items():
        ax.scatter(x, y, s=50)
        ax.text(x + 0.05, y, node.name, ha="left", va="center")

    ax.set_axis_off()
    ax.set_aspect('equal', adjustable='datalim')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    root = parse_tree(data)
    plot_tree(root)
