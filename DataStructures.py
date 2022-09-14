
def format_list(head):
    if head.next is None:
        return f"[{head.get_value()}]-|"
    else:
        return f"[{head.get_value()}]->{format_list(head.next)}"

def sortll(head):
    if head.get_next() is None:
        return head
    elif head.get_next().get_value() < head.get_value():
        #store
        ref = head.get_next().get_next()
        new_head = head.get_next()
        #switch
        head.set_next(ref)
        # set
        new_head.set_next(head)



        return new_head
    else:
        return head


class LinkedList:

    def __init__(self, linkedList, value):
        self.next = linkedList
        self.value = value

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def set_value(self, value):
        self.value = value

# binary tree
class Node:

    def __init__(self, value, leftChildNode, rightChildNode):
        self.value = value
        self.leftNode = leftChildNode
        self.rightNode = rightChildNode

    def addNode(self, Node):
        if Node.value < self.value:
            if self.leftNode is None:
                self.leftNode = Node
            else:
                self.leftNode.addNode(Node)
        else:
            if self.rightNode is None:
                self.rightNode = Node
            else:
                self.rightNode.addNode(Node)

    def print_tree(node):
        Node.print_tree_pretty("", node, False);

    def print_tree_pretty(prefix, node, isLeft):
        if node is not None:
            print_tree_string = prefix
            print_tree_string += "├──" if isLeft else "└──"
            print(print_tree_string + f" {node.value}")

            Node.print_tree_pretty(prefix + ("│   " if isLeft else "    "), node.leftNode, True)
            Node.print_tree_pretty(prefix + ("│   " if isLeft else "    "), node.rightNode, False)
