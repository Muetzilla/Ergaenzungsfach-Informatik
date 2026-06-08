class Knoten:
    def __init__(self, key, data = None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return f"Knoten(key={self.key}, data={self.data})"


    def find(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left:
            return self.left.find(key)
        elif key > self.key and self.right:
            return self.right.find(key)
        return None

    def add(self, knoten):
        if knoten.key < self.key:
            if self.left is None:
                self.left = knoten
            else:
                self.left.add(knoten)
        elif knoten.key > self.key:
            if self.right is None:
                self.right = knoten
            else:
                self.right.add(knoten)

    def print_tree(self, prefix="", is_left=True):
        if self.right:
            self.right.print_tree(
                prefix + ("│   " if is_left else "    "),
                False
            )

        print(prefix + ("└── " if is_left else "┌── ") + str(self.key))

        if self.left:
            self.left.print_tree(
                prefix + ("    " if is_left else "│   "),
                True
            )


wurzel = Knoten(32)
wurzel.add(Knoten(15))
wurzel.add(Knoten(47))
wurzel.add(Knoten(9))
wurzel.add(Knoten(24))
wurzel.add(Knoten(6))
wurzel.add(Knoten(11))
wurzel.add(Knoten(5))
wurzel.add(Knoten(7))
wurzel.add(Knoten(22))
wurzel.add(Knoten(27))
wurzel.add(Knoten(16))
wurzel.add(Knoten(46))
wurzel.add(Knoten(63))
wurzel.add(Knoten(49))


print(wurzel.find(22))
print(wurzel.find(49))
print(wurzel.find(11))
print(wurzel.find(6))
print(wurzel.find(15))
print()
print("=" * 50)
print()
print(wurzel.print_tree())