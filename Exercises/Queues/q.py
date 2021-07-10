class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def size(self) -> int:
        return self.size
    
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