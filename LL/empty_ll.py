###############################################################################
'''
Linked List Operations
1. Insert: a) head b) tail(append) c) middle(insert)
2. Delete: a) head b) tail(pop) c) value(remove) d) index
3. Traverse: a) print
4. Search: a) value b) index
'''
###############################################################################


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        # Creating empty  LL
        self.head = None
        self.n = 0    # n tells you how many nodes are there in LL  

    def __len__(self):
        return self.n 
        


L = LinkedList()       
print(L) 
print(len(L))      