class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self
        self.visited = False
        self.parent = None

    def setToVisited(self):
        self.visited = True
