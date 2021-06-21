class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node = None
        self.prev: Node = None
    
    def draw(self):
        print(self.value)
        
        if self.prev:
            print("\t__nodeprev__: ", self.prev.value)   
        if self.next:
            print("\t__nodenext__: ", self.next.value)
            print("""\t\t
                        |
                      \ | /
                        *""")
        print("\n")


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    # increment self.size by 1
    def i(self):
        self.size += 1
    
    # decrement self.size by 1
    def d(self):
        self.size -= 1

    def draw(self):
        if self.size == 0:
            print("list is empty")

        elif self.size == 1:
            print("__listhead__: ", self.head.draw())

        else:
            cur = self.head
            self.head.draw()
            while cur.next:
                cur = cur.next
                cur.draw()        

    # return the Node at the given index
    # return None if there's not a Node with the index
    def node_at(self, index: int):
        cur = self.head
        idx = 0

        if cur:
            if index == idx:
                return cur

            while cur.next:
                cur = cur.next
                idx += 1
                
                if index == idx:
                    return cur
                
        return None

    # add a node at the end of the list
    def append(self, node: Node):
        if self.size == 0:
            self.head = node  
            self.i()

        elif self.size == 1:
            self.head.next = node
            node.prev = self.head
            self.i()

        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            node.prev = cur
            cur.next = node
            self.i()

    # add a node at the beginning of the list
    def prepend(self, node: Node):
        if self.size == 0:
            self.head = node    
            self.i()

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.i()
    
    # add node_to_add after node
    def add_after(self, node: Node, node_to_add: Node):
        if node.next:           
            node_to_add.next = node.next
            node_to_add.next.prev = node_to_add
            node.next = node_to_add
            node_to_add.prev = node
            self.i()
        # add a node after the last element
        else:
            self.append(node_to_add)
            self.i()

    def add_before(self, node: Node, node_to_add: Node):
        if node.prev:  
            node_to_add.next = node
            node_to_add.prev = node.prev
            node.prev.next = node_to_add
            node.prev = node_to_add
            self.i()

        else:
            node_to_add.next = node
            node.prev = node_to_add
            self.head = node_to_add
            self.i()

    def delete(self, node: Node):
        if node == None: 
            raise Exception("node is None")

        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None
            self.d()

        elif node.prev:
            node.prev.next = None
            node.prev = None
            self.d()

        elif node.next:
            self.head = node.next
            node.next.prev = None
            node.next = None
            self.d()
        else:
            self.head = None
            self.d()

    def pop(self) -> Node:
        if self.size == 0:
            raise Exception("list is empty")
        to_pop = self.node_at(0)
        self.delete(to_pop)
        return to_pop

    """
        I tried reversing the list before watching any video about reversing a linked list,
        but didn't quite managed to get it right.
        Here's the video explaining how to reverse a linked list:
        https://youtu.be/SQHvcLvqq_Q
    """
    def reverse(self):
        tmp = None
        cur = self.head         #self.head.prev == None
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev

    def insert_at(self, index: int, node: Node):
        if index == 0:
            self.prepend(node)
            self.i()
        elif index == 1:
            self.add_after(self.node_at(0), node)
            self.i()
        elif index == self.size - 1:
            self.append(node)
        else:
            try:
                self.add_after(self.node_at(index - 1), node)
                self.i()
            except TypeError:
                raise Exception("cannot add node to index: " + index)

""" TESTS"""

dll = DoublyLinkedList()

n1 = Node("FIRST NODE")
dll.append(n1)

n2 = Node("SECOND NODE")
dll.append(n2)

n3 = Node("THIRD NODE")
dll.append(n3)
"""
print(dll.head.value)
print(dll.head.next.value)
print(dll.head.next.next.value)
"""
"""
print(" <PREPEND> ")

n4 = Node("PREPEND ME")
dll.prepend(n4)

print(dll.head.value)
print(dll.head.next.value)
print(dll.head.next.next.value)
print(dll.head.next.next.next.value)
"""

#print(" <ADD AFTER> ")

n4 = Node("ADD AFTER FIRST NODE")
dll.add_after(dll.node_at(0), n4)
"""
print(dll.head.value)
print(dll.head.next.value)
print(dll.head.next.next.value)
print(dll.head.next.next.next.value)

"""

n5 = Node("ADD BEFORE 'ADD AFTER FIRST NODE'")
dll.add_before(dll.node_at(1), n5)

n6 = Node("ADD BEFORE FIRST NODE")
dll.add_before(dll.node_at(0), n6)

#dll.draw()

#dll.delete(dll.node_at(0))              # first CHECK
#dll.delete(dll.node_at(2))              # middle CHECK
#dll.delete(dll.node_at(dll.size - 1))   # last CHECK
"""
print(" <AFTER DELETING SOME> ")

dll.draw()

"""
"""
print("POPPED: ", dll.pop().value)

dll.draw()
"""
"""
print("\n\n <REVERSED> \n\n")

dll.reverse()

dll.draw()
"""
"""
n7 = Node("WAY BEFORE ANY NODE")
dll.insert_at(0, n7)

n8 = Node("MIDDLISH")
dll.insert_at(3, n8)
"""
n9 = Node("LAST")
dll.insert_at(dll.size - 1, n9)

dll.draw()
