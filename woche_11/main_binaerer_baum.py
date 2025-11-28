from mylib.Suchbaum import Suchbaum
from mylib.Baumknoten import Baumknoten
import random

# -- init Baumknoten --
eris = Baumknoten(136199, "Eris", "2003 UB313", None, None, None)
crantor = Baumknoten(83982, "Crantor", "2002 GO9", None, None, None)
echeclus = Baumknoten(60558, "Echeclus", "2000 EC98", None, None, None)
bienor = Baumknoten(54598, "Bienor", "2000 QC243", None, None, None)
sedna = Baumknoten(90377, "Sedna", "2003 VB12", crantor, eris, None)
amycus = Baumknoten(55576, "Amycus", "2002 GB10", bienor, echeclus, None)
ceto = Baumknoten(65489, "Ceto", "2003 FX128", amycus, sedna, None)
amycus.parent = ceto
sedna.parent = ceto
bienor.parent = amycus
echeclus.parent = amycus
crantor.parent = sedna
eris.parent = sedna

# -- init Suchbaum --
suchbaum = Suchbaum(ceto)


print(suchbaum.anker) #Ceto: 2003 FX128
print("-", suchbaum.anker.left_child) #- Amycus: 2002 GB10
print("--", suchbaum.anker.left_child.left_child)   #-- Bienor: 2000 QC243
print("--", suchbaum.anker.left_child.right_child) #-- Echeclus: 2000 EC98
print("-", suchbaum.anker.right_child) #- Sedna: 2003 VB12
print("--", suchbaum.anker.right_child.left_child)  #-- Crantor: 2002 GO9
print("--",suchbaum.anker.right_child.right_child) #-- Eris: 2003 UB313


# -- Suche --
knoten = suchbaum.suchen(55576)
print("Gefunden:", knoten)

knoten = suchbaum.suchen(99999)
print("Gefunden:", knoten)


print(suchbaum)
# -- Einfügen --
new_knoten_1 = Baumknoten(70000, "Erde", "2025 ABC", None, None, None)
new_knoten_2 = Baumknoten(12351, "Mars", "2025 ABC", None, None, None)
new_knoten_3 = Baumknoten(99812, "Merkur", "2025 ABC", None, None, None)
new_knoten_4 = Baumknoten(99999, "Jupiter", "2025 ABC", None, None, None)
new_knoten_5 = Baumknoten(999551, "Venus", "2025 ABC", None, None, None)
new_knoten_6 = Baumknoten(122020, "Europa", "2025 ABC", None, None, None)
new_knoten_7 = Baumknoten(122022, "IO", "2025 ABC", None, None, None)
new_knoten_8 = Baumknoten(122019, "Juno", "2025 ABC", None, None, None)
# suchbaum.insertNode(new_knoten_1)
# suchbaum.insertNode(new_knoten_2)
# suchbaum.insertNode(new_knoten_3)
# suchbaum.insertNode(new_knoten_4)
# suchbaum.insertNode(new_knoten_5)
# suchbaum.insertNode(new_knoten_6)
# suchbaum.insertNode(new_knoten_7)
# suchbaum.insertNode(new_knoten_8)
suchbaum.insertNode(new_knoten_8)
# suchbaum.insertNode(new_knoten_8)

zweiter_baum = Suchbaum(None)
zweiter_baum.insert(100, "Saturn", "2025 DEF")

for i in range(500):
    knoten = Baumknoten(random.randrange(1, 200), f"Knoten_{i}", "2025 XYZ", None, None, None)
    if zweiter_baum.suchen(knoten.key) is None:
        zweiter_baum.insertNode(knoten)

# zweiter_baum.plot()

suchbaum.plot()
print("--Preorder Traversal--")
print(suchbaum.preorder_traversal(suchbaum.anker, []))
print("--Postorder Traversal--")
print(suchbaum.postorder_traversal(suchbaum.anker, []))
print("--Inorder Traversal--")
print(suchbaum.inorder_traversal(suchbaum.anker, []))
print("--Güte des Baumes--")
print(zweiter_baum.guete())
