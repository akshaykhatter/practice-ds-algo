class Node:

    def __init__(self, value: int):
        self.value = value
        self.link = None
    
    def __repr__(self):
        return f'<Node {self.value}>'


class LinkedList:
    """
    We store the end pointer here, instead of the head pointer
    """

    def __init__(self):
        self.end = None

    def __repr__(self):
        rep = 'Linked list: '
        # linked list exists
        if self.end is not None:
            iterator = self.end.link
            while iterator.link != self.end.link:
                rep = rep + str(iterator.value) + ' '
                iterator = iterator.link
            rep = rep + str(iterator.value)
        return rep

    def insert_start(self, value: int): # O(1)
        new_node = Node(value)        
        # no linked list exists
        if self.end is None:
            self.end = new_node
            self.end.link = self.end
        else:
            new_node.link = self.end.link
            self.end.link = new_node
    
    def insert_end(self, value: int): # O(1)
        new_node = Node(value)
        # no linked list exists
        if self.end is None:
            self.end = new_node
            self.end.link = self.end
        else:
            new_node.link = self.end.link
            self.end.link = new_node
            self.end = new_node
    
    def delete_start(self): # O(1)
        # linked list exists
        if self.end is not None:
            # if only one node exists
            if self.end.link == self.end:
                self.end = None
            else:
                self.end.link = self.end.link.link
    
    def delete_end(self): # O(n)
        # linked list exists
        if self.end is not None:
            # if only one node exists
            if self.end.link == self.end:
                self.end = None
            else:
                iterator = self.end.link
                while iterator.link != self.end:
                    iterator = iterator.link
                iterator.link = self.end.link
                self.end = iterator

