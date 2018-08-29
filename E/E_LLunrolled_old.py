import math

class Node:

    def __init__(self, value):
        self.value = value
        self.link = None
    
    def __repr__(self):
        return f'<Node {self.value}>'


class LinkedList:

    def __init__(self):
        self.end = None
        self.count = 0
    
    def __repr__(self):
        rep = 'Linked list: '
        values = []
        # linked list exists
        if self.end is not None:
            iterator = self.end.link
            while iterator != self.end:
                values.append(iterator.value)
                iterator = iterator.link
            values.append(iterator.value)
            values.reverse()
            for value in values:
                rep = rep + str(value) + ' '
        return rep

    def get_count(self) -> int:
        return self.count

    def insert(self, value: int): # insert end
        new_node = Node(value)
        self.count = self.count + 1
        # no linked list exists
        if self.end is None:
            self.end = new_node
            self.end.link = self.end
        else:
            new_node.link = self.end.link
            self.end.link = new_node
            self.end = new_node
    
    def remove(self): # delete front
        # linked list exists
        if self.end is not None:
            self.count = self.count - 1
            # only one element in linked list
            if self.end.link == self.end:
                value = self.end.value
                self.end = None
                return value
            else:
                value = self.end.link.value
                self.end.link = self.end.link.link
                return value
        else:
            print('Deletion cannot be performed! No node in linked list')


class Unrolled:

    def __init__(self, initial_size: int):
        self.count = 0
        self.initial_size = initial_size
        self.size = initial_size
        self.meta_list = []
    
    def __repr__(self):
        rep = ''
        for cll in self.meta_list:
            rep = rep + ' | ' + str(cll)
        return rep
    
    def insert(self, value: int):
        self.count = self.count + 1
        if len(self.meta_list) == 0:
            cll = LinkedList()
            cll.insert(value)
            self.meta_list.append(cll)
        else:
            first_cll = self.meta_list[0]
            first_cll.insert(value)
            if self.count <= self.initial_size:
                pass
            else:
                new_size = math.floor(self.count**0.5)
                if new_size != self.size:
                    self.size = new_size
                    self.maintain_limit(0, True)
                else:
                    self.maintain_limit(0, False)
    
    def maintain_limit(self, start_index: int, resize: bool):
        for i in range(start_index, len(self.meta_list)):
            cll = self.meta_list[i]
            if cll.get_count() <= self.size:
                print('maintain limit break')
                break
            else:
                # print('maintain limit no break')
                extra_count = cll.get_count() - self.size
                extra_values = []
                for e in range(extra_count):
                    extra_values.append(cll.remove())
                next_cll = None
                try:
                    next_cll = self.meta_list[i+1]
                except IndexError:
                    next_cll = LinkedList()
                    self.meta_list.append(next_cll)
                for value in extra_values:
                    next_cll.insert(value)
                self.maintain_limit(start_index + 1, False)




ur = Unrolled(3)
ur.insert(6)
ur.insert(5)
ur.insert(7)
ur.insert(8)
ur.insert(9)
ur.insert(10)
ur.insert(11)
ur.insert(12)
ur.insert(13)
print(ur)


