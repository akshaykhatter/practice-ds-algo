class Node:

    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f'<Node {self.value}>'


class LinkedList:

    def __init__(self):
        self.head = None
    
    def __repr__(self): # O(n)
        rep = "Linked list: "
        if self.head is not None:
            iterator = self.head
            while iterator.next != self.head:
                rep = rep + str(iterator.value) + ' '
                iterator = iterator.next
            rep = rep + str(iterator.value)
        return rep
    
    def insert_start(self, value: int): # O(1)
        new_node = Node(value)
        # no linked list exists
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_end(self, value: int): # O(1)
        new_node = Node(value)
        # no linked list exists
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            self.head.prev.next = new_node
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
    
    def delete_start(self): # O(1)
        # linked list exists
        if self.head is not None:
            # only one element exists
            if self.head.next == self.head:
                self.head = None
            else:
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
    
    def delete_end(self): # O(1)
        # linked list exists
        if self.head is not None:
            # only one element exists
            if self.head.next == self.head:
                self.head = None
            else:
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
