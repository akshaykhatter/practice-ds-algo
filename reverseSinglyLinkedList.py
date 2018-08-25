class Node:

    def __init__(self, value: int):
        self.value = value
        self.link = None


class LinkedList:

    def __init__(self):
        self.head = None
    
    def __repr__(self):
        rep = 'Linked List: '
        if self.head is not None:
            iterator = self.head
            while iterator is not None:
                rep = rep + str(iterator.value) + ' '
                iterator = iterator.link 
        return rep
    
    def add(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.link = self.head
            self.head = new_node
    
    def reverse(self):
        if self.head is not None:
            p1 = None
            p2 = self.head
            while p2 is not None:
                p2_next = p2.link
                p2.link = p1
                p1 = p2
                p2 = p2_next
            self.head = p1

ll = LinkedList()
ll.add(5)
ll.add(6)
ll.add(7)
ll.reverse()
print(ll)
