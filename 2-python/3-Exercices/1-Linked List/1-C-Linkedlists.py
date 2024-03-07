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

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self,prev_node,new_data):
        if prev_node is None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

llist = Linkedlist()

first = Node(1)
second = Node(2)
third = Node(3)

llist.head = first
llist.head.next = second
second.next = third

llist.push(0)
llist.insert(second,9)
llist.print_list()
