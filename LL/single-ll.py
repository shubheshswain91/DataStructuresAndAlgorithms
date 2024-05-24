class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    '''
    This class creates Nodes at various positions and to create the node we call the Node Class.
    '''

    def __init__(self, value):
        new_node = Node(value)      # create a node
        self.head = new_node
        self.tail = new_node
        self.length = 1       # represents the current number of nodes in the list.

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        '''
        We are taking two temporary variables temp and pre and initially assign it with the head node
        '''

        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        '''
            In the below while loop we are traversing till the last node i.e with the next value is None. In each iteration we are updating the pre 
            node with the next temp node and the temp node goes to the next node while the pre node remains one node behind.
            At the end node when the temp->next is None, the while becomes false and we come out of it.
        '''
        while(temp.next):  
            pre = temp 
            temp = temp.next
        '''
            Now that we have the second last node saved in the pre node, we can update the tail node with it and make the tail->next = None and also 
            decrement the length value.
        '''    
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:   # condition to check if there is no node
            self.head = None
            self.tail = None
        return temp    


    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0        

my_ll = LinkedList(4)
my_ll.make_empty()
my_ll.append(4)
my_ll.append(5)
my_ll.print_list()
my_ll.pop()
my_ll.print_list()
my_ll.pop()
my_ll.print_list()
my_ll.pop()
my_ll.print_list()


# print(my_ll.head.value)
# print(my_ll.tail.value)
# print(my_ll.length)
