class Baumknoten:
    def __init(self, num, name, identifier, left_child, right_child):
        self.num = num
        self.name = name
        self.identifier = identifier
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return f"Baumknoten(num={self.num}, name={self.name}, identifier={self.identifier})"