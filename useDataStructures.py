from DataStructures import LinkedList, format_list, sort

tail = LinkedList(None, 1)
head = LinkedList(None, 2)

head.set_next(tail)
tail.set_next(LinkedList(None,3))

head = sort(head)

print(format_list(head))
