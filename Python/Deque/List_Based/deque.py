"""
    Deque data structure implementation using a Python list.
    A deque is like a combination of a stack and a queue.

    Learn about deques: 
        https://bradfieldcs.com/algos/deques/introduction/
        https://www.programiz.com/dsa/deque
        https://en.wikipedia.org/wiki/Double-ended_queue
"""

"""
                            REAR                FRONT
                             |                    |
                             v                    v    
REMOVE_REAR || ADD_REAR --  [1, 2, 3, 4, 5, 6, 7, 8]  -- REMOVE_FRONT || ADD_FRONT
"""

class Deque:
    def __init__(self) -> None:
        self.__items = []
        self.__rear = None
        self.__front = None
        self.__size = 0
    
    def get_size(self) -> int:
        s = self.__size
        return s

    def add_front(self, value: any):
        self.__items.append(value)
        if self.get_size() == 0:
            self.__rear = self.__items[0]
            self.__front = self.__items[0]
        else:   
            self.__front = self.__items[-1]
        self.__size += 1
    
    def add_rear(self, value: any):
        self.__items.insert(0, value)
        if self.get_size() == 0:
            self.__front = self.__items[0]
        self.__rear = self.__items[0]
        self.__size += 1

    def remove_front(self) -> any:
        if self.get_size() == 0:
            raise Exception("deque is empty")
        elif self.get_size() == 1:
            self.__front = None
            removed = self.__items.pop()
            self.__size -= 1
            return removed
        else:
            self.__front = self.__items[-2]
            removed = self.__items.pop()
            self.__size -= 1
            return removed
    
    def remove_rear(self) -> any:
        if self.get_size() == 0:
            raise Exception("deque is empty")
        elif self.get_size() == 1:
            self.__rear = None
            removed = self.__items.pop(0)
            self.__size -= 1
            return removed
        else:
            self.__rear = self.__items[1]
            removed = self.__items.pop(0)
            self.__size -= 1
            return removed
    
    def is_empty(self) -> bool:
        return self.__size == 0
    
    def items(self) -> list[any]:
        i = self.__items
        return i


dq = Deque()

print(dq.get_size())

print(" <ADD REAR 'Hello'> ")
dq.add_rear("Hello")
print(dq.get_size())
print(dq.items())

print(" <ADD FRONT 'HEY'> ")
dq.add_front("HEY")
print(dq.get_size())
print(dq.items())

print(" <REMOVE REAR ONE> ")
dq.remove_rear()
print(dq.get_size())
print(dq.items())

print(" <REMOVE FRONT ONE> ")
dq.remove_front()
print(dq.items())
