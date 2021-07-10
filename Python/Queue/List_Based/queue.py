"""
   REAR        FRONT
    |            |
    v            v
    [1, 2, 3, 4, 5] --> dequeue
"""


class Queue:
    def __init__(self) -> None:
        self.__items = []
        self.__size = 0
        self.__front = None
        self.__rear = None
    
    def get_size(self) -> int:
        s = self.__size
        return s

    # ** O(n)
    def enqueue(self, item: any):
        # * because of this insert
        self.__items.insert(0, item)
        self.__front = self.__items[0]

        if self.get_size() == 0:
            self.__rear = self.__items[0]
        
        self.__size += 1

    # ** O(1)
    def dequeue(self):
        if self.get_size() == 0:
            raise Exception("queue is empty")
        elif self.get_size() == 1:
            self.__front = None
            self.__rear = None
        else:
            prev_front = self.__items[-2]
            self.__front = prev_front
            # * pop is O(1)
            self.__items.pop()
        self.__size -= 1
    
    def is_empty(self):
        return self.get_size() == 0

    def items(self) -> list:
        i = self.__items
        return i 

q =  Queue()
print(q.get_size())

q.enqueue("FIRST")

print(q.get_size())

q.enqueue("SECOND")

print(" <ADD TWO ITEMS> ")

print(q.items())

q.dequeue()

print(" <DEQUEUE ONE> ")

print(q.items())
print(q.get_size())

print(" <DEQUEUE ONE MORE> ")
q.dequeue()
print(q.get_size())

print(q.items())

print(" <DEQUEUE ONE MORE> ")
#q.dequeue() # Exception

