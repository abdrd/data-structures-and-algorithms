"""
    Queue data structure implementation in Python programming language.
    (Based on a doubly linked list)

    Learn about queues:
        https://www.tutorialspoint.com/data_structures_algorithms/dsa_queue.htm
        https://www.studytonight.com/data-structures/queue-data-structure
        https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
    
    Representation
        Node: []

              FRONT       REAR / TAIL  
                |           |
                v           v
   <- dequeue  [] [] [] [] []    <- enqueue 
"""

# * NODE 
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self) -> None:
        # * front points to the node at the index where the next dequeue operation will be performed on.
        self.front = None
        # * rear points to the location where the next enqueue operation will be performed.
        self.rear = None
        # * size of the queue
        self.size = 0
    
    def size(self) -> int:
        return self.size
    
    # ** O(1)
    # * we could've used a expected a value instead of a Node
    def enqueue(self, node: Node):
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            # * prev rear
            rear = self.rear
            self.rear = node
            node.prev = rear
            rear.next = node
        self.size += 1
    
    # ** O(1)
    def dequeue(self):
        if self.size == 0:
            raise Exception("queue is empty")
        elif self.size == 1:
            self.front = None
            self.rear = None
            self.size -= 1
        else:
            tmp = self.front
            self.front = self.front.next
            self.front.prev = None
            tmp.next = None
            self.size -= 1

    # * return a copy of the front node of the queue 
    def peek(self) -> Node:
        if self.size == 0:
            raise Exception("queue is empty")
        else:
            tmp = self.front
            return tmp
        
    def is_empty(self) -> bool:
        if self.size == 0:
            return True
        return False

"""TEST"""

q = Queue()

#print(q.is_empty())

# q.dequeue() #* Exception: queue is empty

n1 = Node(1)
q.enqueue(n1)
"""
print(q.front.value)

q.dequeue()

print(q.front)
"""
#print(q.front.value)
#print(q.rear.value)

n2 = Node(2)
q.enqueue(n2)
"""
print("SIZE: ", q.size)
print(q.front.value)
print(q.rear.value)
print(q.front.next.value)
print(q.rear.prev.value)
"""
n3 = Node(3)
q.enqueue(n3)
"""
print("SIZE: ", q.size)
print(q.front.value)
print(q.rear.value)
print(q.front.next.value)
print(q.rear.prev.value)
"""
"""
q.dequeue()

print(" <DEQUEUE> ")

print("SIZE: ", q.size)
print(q.front.value)
print(q.rear.value)
print(q.front.next)
print(q.rear.prev)
"""
"""
q.dequeue()

print("SIZE: ", q.size)
print(q.front.value)
print(q.rear.value)
print(q.front.next.value)
print(q.rear.prev.value)
"""
#q.dequeue()
#q.dequeue()
#q.dequeue()

#print(q.peek().value)
#print(q.is_empty())
