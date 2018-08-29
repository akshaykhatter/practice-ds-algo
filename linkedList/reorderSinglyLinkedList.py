# If original list is like 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# Then make it like 1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4 -> 8 # reorder_1
# and also like 1 -> 8 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5 # reorder_2

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
        # detect middle of the linked list using fast and slow pointer
        iterator_A = iterator_B = self.head
        
        # there may be odd no of nodes in ll, hence need to check iterator_B.link first
        while iterator_B.link is not None and iterator_B.link.link is not None:
            iterator_A = iterator_A.link
            iterator_B = iterator_B.link.link
        
        # Breaking the linked list into two halves, first half starts from self.heaf and second part from iterator_A
        temp = iterator_A
        iterator_A = iterator_A.link
        temp.link = None

        ###

        # reorder linked list
        i = self.head
        j = iterator_A

        while i is not None and j is not None:
            i_next = i.link
            i.link = j
            j_next = j.link
            j.link = i_next

            i = i_next
            j = j_next


    def reorder_2(self):
        # detect middle of the linked list using fast and slow pointer
        iterator_A = iterator_B = self.head
        
        # there may be odd no of nodes in ll, hence need to check iterator_B.link first
        while iterator_B.link is not None and iterator_B.link.link is not None:
            iterator_A = iterator_A.link
            iterator_B = iterator_B.link.link
        
        # Breaking the linked list into two halves, first half starts from self.heaf and second part from iterator_A
        temp = iterator_A
        iterator_A = iterator_A.link
        temp.link = None

        ###

        # reverse second half of linked list
        p1 = None
        p2 = iterator_A

        while p2 is not None:
            p2_next = p2.link
            p2.link = p1
            p1 = p2
            p2 = p2_next
        iterator_A = p1

        ###

        # reorder linked list
        i = self.head
        j = iterator_A

        while i is not None and j is not None:
            i_next = i.link
            i.link = j
            j_next = j.link
            j.link = i_next

            i = i_next
            j = j_next
    


ll = LinkedList()
ll.insert(8)
ll.insert(7)
ll.insert(6)
ll.insert(5)
ll.insert(4)
ll.insert(3)
ll.insert(2)
ll.insert(1)
# ll.reorder_1()
ll.reorder_2()
print(ll)