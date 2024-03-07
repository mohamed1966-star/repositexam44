class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next

llist = Linkedlist()

first = Node(1)
second = Node(2)
third = Node(3)

llist.head = first
llist.head.next = second
second.next = third


llist.print_list()
