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
        rep = 'Doubly linked list: '
        iterator = self.head
        while iterator is not None:
            rep = rep + str(iterator.value) + " "
            iterator = iterator.next
        return rep
    
    def count_nodes(self): # O(n)
        count = 0
        iterator = self.head
        while iterator is not None:
            count = count + 1
            iterator = iterator.next
        return count
    
    def insert_start(self, value: int): # O(1)
        new_node = Node(value)
        # no linked list exists
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, value: int): # O(n)
        new_node = Node(value)
        # no linked list exists
        if self.head is None:
            self.head = new_node
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            iterator.next = new_node
            new_node.prev = iterator
    
    def insert_middle(self, value: int, position: int): # O(pos)
        new_node = Node(value)
        total_nodes = self.count_nodes()
        if total_nodes < 2:
            print("Middle position doesn't exist, first add elements at the start or end")
        elif position == 0:
            print("Attempting to add nodes at the start, please use insert_start method")
        elif position >= total_nodes:
            print("Invalid index for middle position")
        else:
            iterator = self.head
            count = 0
            while count != position - 1:
                count = count + 1
                iterator = iterator.next
            # connection between new_node and iterator.next
            new_node.next = iterator.next
            iterator.next.prev = new_node
            # connection between iterator and new_node
            new_node.prev = iterator
            iterator.next = new_node
    
    def delete_start(self): # O(1)
        # linked list exists
        if self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next
    
    def delete_end(self): # O(n)
        # linked list exists
        if self.head is not None:
            iterator = self.head
            while iterator.next.next is not None:
                iterator = iterator.next
            iterator.next = None
    
    def delete_middle(self, position: int): # O(pos)
        total_nodes = self.count_nodes()
        if total_nodes < 3:
            print("Middle position doesn't exist")
        elif position == 0 or position == total_nodes - 1:
            print("Attempting to delete the first or last node, please use other methods")
        elif position >= total_nodes:
            print("Invalid index for middle position")
        else:
            count = 0
            iterator = self.head
            while count != position - 1:
                count = count + 1
                iterator = iterator.next
            iterator.next.next.prev = iterator
            iterator.next = iterator.next.next
