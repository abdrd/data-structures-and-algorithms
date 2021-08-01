"""
    Stack implemented with an underlying doubly linked list.
    This is very similar to a stack using a singly linked list.
    (almost identical)
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev: Node = None
        self.next: Node = None

    def draw(self):
        print(f"""[ {self.value} ]""")

class Stack:
    top: Node = None
    size: int = 0

    def i(self):
        self.size += 1
    def d(self):
        self.size -= 1

    def draw(self):
            if self.top:
                cur = self.top
                cur.draw()
                while cur.next:
                    cur = cur.next
                    cur.draw()

    def push(self, node: Node):
        if self.top:
            cur = self.top
            node.next = cur
            cur.prev = node
            self.top = node
            self.i()
        else: # self.top is None
            self.top = node
            #increment self.size 
            self.i()
 
    def pop(self) -> Node:
        if self.size == 0:
            raise Exception("cannot pop - stack is empty")

        to_pop = self.top

        if self.top.next:
            self.top = self.top.next

        to_pop.next = None
        self.d()

        return to_pop
    
    def peek(self) -> Node:
        if self.size == 0:
            raise Exception("cannot peek - stack is empty")

        to_peek = self.top

        return to_peek

    def is_empty(self) -> bool:
        if self.size == 0 or self.top == None:
            return True
        return False
    
    def remove_top(self):
        if self.size == 0:
            raise Exception("cannot remove_top - stack is empty")
        
        if self.top:
            if self.top.next:
                cur = self.top
                self.top = cur.next
                self.top.prev = None
                cur.next = None
                self.d()
            else: # no node under self.top 
                cur = self.top
                self.top = None
                cur.next = None
                self.d()

   
s = Stack()

#print(s.size)

n1 = Node(1)
s.push(n1)
"""
print(s.size)
print(s.top.value)
"""
n2 = Node(2)
s.push(n2)

n3 = Node(3)
s.push(n3)
"""
print(s.size)

print(s.top.value)
"""

s.draw()


