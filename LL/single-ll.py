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

# print(my_ll.head.value)
# print(my_ll.tail.value)
# print(my_ll.length)
