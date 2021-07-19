"""
    Deque (using a doubly linked list)
          REAR                FRONT
           |                    |
           v                    v
   NULL <- [] <-> [] <-> [] <-> [] -> NULL
"""

# TODO remove ops buggy (probably) 
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.prev: Node = None
        self.next: Node = None

class Deque:
    def __init__(self) -> None:
        self.size = 0
        self.front: Node = None
        self.rear: Node = None

    def add_front(self, value):
        node_to_add = Node(value)
        if self.size == 0:
            self.front = node_to_add
            self.rear = node_to_add
            self.size += 1
        else:
            tmp = self.front
            self.front.next = node_to_add
            node_to_add.prev = tmp
            self.front = node_to_add
            self.size += 1
    
    def remove_front(self) -> Node:
        if self.size == 0:
            raise Exception("deque is empty")
        elif self.size == 1:
            front = self.front
            self.front = None
            self.rear = None
            self.size -= 1
            return front
        else:
            front = self.front
            before_front = self.front.prev
            front.prev = None
            before_front.next = None
            self.front = before_front
            self.size -= 1
            return front
    
    def add_rear(self, value):
        node_to_add = Node(value)
        if self.size == 0:
            self.rear = node_to_add
            self.front = node_to_add
            self.size += 1
        else:
            rear = self.rear
            self.rear.prev = node_to_add
            node_to_add.next = rear
            self.rear = node_to_add
            self.size += 1
    
    def remove_rear(self) -> Node:
        if self.size == 0:
            raise Exception("deque is empty")
        elif self.size == 1:
            rear = self.rear
            self.rear = None
            self.front = None
            self.size -= 1
            return rear
        else:
            rear = self.rear
            after_rear = rear.next
            rear.next.prev = None
            rear.next = None
            self.rear = after_rear
            self.size -= 1
            return rear

dq = Deque()

print(dq.rear)
print(dq.front)
print(dq.size)

print(" <ADD FRONT 'FIRST'> ")
dq.add_front("FIRST")
print(dq.rear.value)
print(dq.front.value)
print(dq.size)

print(" <ADD REAR 'SECOND'> ")
dq.add_rear("SECOND")
print(dq.rear.value)
print("REAR NEXT: ", dq.rear.next.value)
print(dq.front.value)
print(dq.size)

print(" <REMOVE REAR> ")
removed = dq.remove_rear()
print("REMOVED: ", removed.value)
print(dq.size)
print(dq.front.value)
print(dq.rear.value)

dq.draw()

"""
print(" <ADD A COUPLE OF NODES> ")
dq.add_rear("something 2 ")
dq.add_front("something 3")

print(dq.front.value)
print(dq.rear.value)
print(dq.size)

print(" <REMOVE FRONT> ")
removed = dq.remove_front()
print("REMOVED: ", removed.value)
print(dq.size)
print(dq.front.value)
print(dq.rear.value)"""