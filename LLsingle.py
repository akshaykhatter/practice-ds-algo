class Node:

    def __init__(self, value):
        self.value = value
        self.link = None

    def __repr__(self):
        return f'<Node {self.value}>'


class LinkedList:

    def __init__(self):
        self.head = None
    
    def __repr__(self): # O(n)
        rep = "Linked List: "
        iterator = self.head
        while iterator is not None:
            rep = rep + str(iterator.value) + " "
            iterator = iterator.link
        return rep
    
    def count_nodes(self) -> int: # O(n)
        count = 0
        iterator = self.head
        while iterator is not None:
            count = count + 1
            iterator = iterator.link
        return count

    def insert_start(self, value: int): # O(1)
        new_node = Node(value)
        # no linked list exists
        if self.head is None:
            self.head = new_node
        else:
            new_node.link = self.head
            self.head = new_node

    def insert_end(self, value: int): # O(n)
        new_node = Node(value)
        # no linked list exists
        if self.head is None:
            self.head = new_node
        else:
            iterator = self.head
            while iterator.link is not None:
                iterator = iterator.link
            iterator.link = new_node

    def insert_middle(self, value: int, position: int): # position is index O(pos)
        new_node = Node(value)
        total_nodes = self.count_nodes()
        if total_nodes <=1:
            print("Middle position doesn't exist yet, insert elements at start or end first")
        elif position == 0:
            print("Attempting to insert elements at the start, please use insert_start method")
        elif position >= total_nodes:
            print("Invalid index for middle position")
        else:
            iterator = self.head
            count = 0
            while count != position - 1:
                iterator = iterator.link
                count = count + 1
            new_node.link = iterator.link
            iterator.link = new_node   

    def delete_start(self): # O(1)
        # linked list exists
        if self.head is not None:
            # only one element i.e. head exists
            if self.head.link is None:
                self.head = None
            else:
                self.head = self.head.link

    def delete_end(self): # O(n)
        # linked list exists
        if self.head is not None:
            # only one element i.e. head exists
            if self.head.link is None:
                self.head = None
            else:
                iterator = self.head
                # stop at second last element
                while iterator.link.link is not None:
                    iterator = iterator.link
                iterator.link = None

    def delete_middle(self, position: int): # position is index O(pos)
        total_nodes = self.count_nodes()
        if total_nodes < 3:
            print("Middle nodes don't exist yet")
        elif position == 0 or position == total_nodes - 1:
            print("Attempting to delete nodes at the start or end, please use other methods")
        else:
            iterator = self.head
            count = 0
            while count != position - 1:
                count = count + 1
                iterator = iterator.link
            iterator.link = iterator.link.link
