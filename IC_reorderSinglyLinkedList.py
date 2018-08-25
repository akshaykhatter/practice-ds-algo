# If original list is like 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# Then make it like 1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4 -> 8
# and also like 1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5

class Node:
    
    def __init__(self, value):
        self.value = value
        self.link = None


class LinkedList:

    def __init__(self):
        self.head = None
    
    def __repr__(self):
        rep = 'Linked List: '
        iterator = self.head
        while iterator is not None:
            rep = rep + str(iterator.value) + ' '
            iterator = iterator.link
        return rep

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.link = self.head
            self.head = new_node

    def reorder_1(self):
        pass

    def reorder_2(self):
        pass
    


ll = LinkedList()
ll.insert(6)
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.insert(2)
ll.insert(1)
print(ll)