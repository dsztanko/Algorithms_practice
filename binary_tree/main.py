from binary_tree import Service
from node import Node

# This should return a node which has a value 12
n13 = Node(13, None, None)
n12 = Node(12, None, None)
n11 = Node(11, None, None)
n10 = Node(10, None, None)
n9 = Node(9, None, None)
n8 = Node(8, n10, n11)
n7 = Node(7, n12, n13)
n6 = Node(6, None, None)
n5 = Node(5, n8, n9)
n4 = Node(4, None, None)
n3 = Node(3, n6, n7)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

print(Service.find_value(n1, 0))
