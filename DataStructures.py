
def format_list(head):
    if head.next is None:
        return f"[{head.get_value()}]-> None"
    else:
        return f"[{head.get_value()}]->{format_list(head.next)}"

def sort(head):
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
