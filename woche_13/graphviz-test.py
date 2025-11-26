import graphviz
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

output_path = os.path.join(script_dir, "test")

f = graphviz.Digraph(filename=output_path, format="png")

names = ["A", "B", "C", "D", "E", "F", "G", "H"]
positions = ["CEO", "Team A Lead", "Team B Lead", "Staff A", "Staff B", "Staff C", "Staff D", "Staff E"]

for name, position in zip(names, positions):
    f.node(name, position)

f.edge("A", "B"); f.edge("A", "C")     # CEO → Team Leads
f.edge("B", "D"); f.edge("B", "E")     # Team A
f.edge("C", "F"); f.edge("C", "G"); f.edge("C", "H")  # Team B

f.render(cleanup=True)

print("PNG wurde erzeugt unter:", output_path + ".png")
