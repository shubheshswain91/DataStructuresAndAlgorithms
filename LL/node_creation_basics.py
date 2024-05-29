class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
print(f"a's address:{id(a)}(int) and Hex value: {a}")
print(int(0x7ff15280ba90))
# print(a) 
# print(a.value) 
# print(a.next) 

b = Node(2)
print("b's address: ", id(b))
c = Node(3)
print("c's address: ", id(c))
a.next = b
b.next = c
print(f"a's next address:{id(a.next)}(int) and Hex value: {a.next}")
print(f"b's next address:{id(b.next)}(int) and Hex value: {b.next}")
print(f"c's next address:{id(c.next)}(int) and Hex value: {c.next}")
# print(a.next)
# print(a.next.value)