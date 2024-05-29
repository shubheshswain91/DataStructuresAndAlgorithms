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

    def insert_head(self, value):

        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head 

        # reassign head
        self.head = new_node

        # increment n
        self.n += 1

    def __str__(self):
        curr = self.head 
        result = ''
        while curr != None:
            #print(curr.value)
            result = result + str(curr.value) + '->'
            curr = curr.next
        return result    

L = LinkedList()       


L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
#L.traverse()
print(L)
#print(len(L))
