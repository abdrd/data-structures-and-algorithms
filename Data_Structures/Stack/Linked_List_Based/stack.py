"""
    Stack data structure implementation in Python programming language 
    (Dynamic stack, based on a singly linked list)
    Learn about stacks: 
        https://isaaccomputerscience.org/concepts/dsa_datastruct_stack#:~:text=A%20stack%20is%20an%20abstract,the%20top%20of%20the%20stack.
        https://www.geeksforgeeks.org/stack-data-structure/
        https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
"""

class Node:
    def __init__(self, value):
        self.value = value
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

    # value is not a node this time
    def push(self, node: Node):
        if self.top:
            cur = self.top
            node.next = cur
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

    # return the top node without removing it (unlike pop)
    def peek(self) -> Node:
        if self.size == 0:
            raise Exception("cannot peek - stack is empty")

        to_peek = self.top

        return to_peek

    # return false if the stack is empty.
    # if top of the stack is None, this means 
    # the stack is empty
    def is_empty(self) -> bool:
        if self.size == 0 or self.top == None:
            return True
        return False

    # remove the top element, do not return it (unline pop) 
    def remove_top(self):
        if self.size == 0:
            raise Exception("cannot remove_top - stack is empty")
        
        if self.top:
            if self.top.next:
                cur = self.top
                self.top = cur.next
                cur.next = None
                self.d()
            else: # no node under self.top 
                cur = self.top
                self.top = None
                cur.next = None
                self.d()
    
s = Stack()
"""
print(s.size)
print(s.top)
"""
n1 = Node(1)
s.push(n1)
"""
print(s.size)
print(s.top.value)
"""
"""
print(s.size)
popped = s.pop()
print(s.size)
print("popped: ", popped.value)
"""

n2 = Node(2)
s.push(n2)

n3 = Node(3)
s.push(n3)

"""
print(s.top.value)
print(s.top.next.value)
print(s.top.next.next.value)
"""
"""
s.remove_top()
s.remove_top()
s.remove_top()

print(s.is_empty())
"""

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

s.push(n4)
s.push(n5)
s.push(n6)
s.push(n7)
s.push(n8)
s.push(n9)

s.draw()

#print(s.peek().value)