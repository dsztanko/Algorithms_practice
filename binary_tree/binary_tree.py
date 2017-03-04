from node import Node


class Service(object):

    def findValue(node, target_value):
        if node is None:
            return "No node found with value {0} in this binary tree.".format(target_value)
        else:
            print(node.value)
            if node.value == target_value:
                return "Node with value {0} is found: {1}. Target value was: {2}.".format(node.value, node, target_value)
            else:
                node.setToVisited()
                if node.left is None or node.left.visited is True:
                    if node.right is None or node.right.visited is True:
                        if node.parent is None:
                            return "No node found with value {0} in this binary tree.".format(target_value)
                        else:
                            return Service.findValue(node.parent, target_value)
                    else:
                        return Service.findValue(node.right, target_value)
                else:
                    return Service.findValue(node.left, target_value)
