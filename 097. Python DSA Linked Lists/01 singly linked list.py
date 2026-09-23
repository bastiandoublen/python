class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements))

ll = LinkedList()
ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second
second.next = third

print("Linked list elements:")
ll.print_list()
