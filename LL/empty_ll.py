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
        return result[:-2]    
    
    def append(self, value):

        new_node = Node(value)

        if self.head == None:
            # empty 
            self.head = new_node
            self.n += 1
            return
        

        curr = self.head
        '''
        V.Imp
        If you want to stop at particular node starting from the first node, then curr != None, for example 1->2->3, if  you want to stop at 3.
        If you want to stop at 2, then condition will be curr.next != None, if at 1 then curr.next.next != None
        
        '''
        while curr.next != None:
            curr = curr.next

        # you are at the last node 
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):

        new_node = Node(value)

        curr = self.head 

        while curr != None:
            if curr.value == after:
                break 
            curr = curr.next

        # case 1: You found the item i.e., curr -> not None
        if curr != None:
            new_node.next = curr.next 
            curr.next = new_node 
        else:
            return 'Item Not found'    
        # case 2 Item wasn't found and curr.value  is None i.e., curr -> None

        print(curr.value)    



L = LinkedList()       


L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.insert_after(2,200)
#L.traverse()
print(L)
#print(len(L))
L.insert_after(20,200)
L.append(5)
print(L)