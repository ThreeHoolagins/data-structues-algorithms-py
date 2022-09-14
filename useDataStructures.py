from DataStructures import LinkedList, format_list, sortll, Node
import random

def test_linked_list():
    tail = LinkedList(None, 1)
    head = LinkedList(None, 2)

    head.set_next(tail)
    tail.set_next(LinkedList(None,3))

    head = sortll(head)

    print(format_list(head))

def test_tree():
    head = Node(23, None, None)
    for i in range(4):
        rand = random.randint(0,40)
        child = Node(rand, None, None)
        head.addNode(child)

    Node.print_tree(head)

if __name__ == "__main__":
   # test_linked_list()
   test_linked_list()
