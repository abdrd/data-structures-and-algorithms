"""
    Circular linked list implementation using a doubly linked list.

     HEAD                                TAIL
 - >  [] <-> [] <-> [] <-> [] <-> [] <-> [] next ----|
 |   prev                                 ^          |
  |   |___________________________________|          |
  |                                                  |
  |__________________________________________________|
"""

from doubly_linked_list import Node, DoublyLinkedList

class CircularLinkedList(DoublyLinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.tail: Node = None

    def append(self, value):
        node_to_add = Node(value)

        if self.size == 0:
            self.head = node_to_add
            self.tail = node_to_add
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size += 1

        else:
            self.tail.next = node_to_add
            node_to_add.prev = self.tail
            self.tail.next = self.head
            self.head.prev = node_to_add
            self.tail = node_to_add
            self.size += 1
    
    def prepend(self, value):
        node_to_add = Node(value)
        
        if self.size == 0:
            self.head = node_to_add
            self.tail = node_to_add
            self.head.prev = self.tail
            self.tail.next = self.head
            self.size += 1

        else:
            self.head.prev = node_to_add
            node_to_add.next = self.head
            self.tail.next = node_to_add
            node_to_add.prev = self.tail
            self.head = node_to_add


cll = CircularLinkedList()
print(cll.head)
print(cll.tail)
print(cll.size)

"""
cll.prepend("PREPEND - cll is empty")
print(cll.head.value)
print(cll.tail.value)
print(cll.head.next.value)
print(cll.tail.prev.value)
print(cll.size)
"""

print(" <APPENDED FIRST> ")
cll.append("APPENDED FIRST")
print(cll.head.value)
print(cll.tail.value)
print(cll.size)

print(" <PREPENDED FIRST> ")
cll.prepend("PREPENDED FIRST")
print(cll.head.value)
print(cll.tail.value)
print(cll.size)
print(cll.head.next.value)
print(cll.tail.prev.value)

print(" <APPENDED SECOND> ")
cll.append("APPENDED SECOND")
print(cll.head.value)
print(cll.tail.value)
print(cll.size)
print(cll.head.next.next.value)
print(cll.tail.prev.value)
