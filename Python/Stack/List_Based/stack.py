class StackIsEmptyException(Exception):
    pass

# TOP
#  |
#  v
# [1, 2, 3, 4]

class Stack:
    def __init__(self) -> None:
        self.__items = []
        self.__size = 0
    
    def __str__(self) -> str:
        return f"STACK ITEMS: {self.__items}"

    def peek(self):
        if self.__size == 0:
            raise StackIsEmptyException
        to_return = self.__items[0]
        return to_return
    
    def push(self, value):
        self.__items.insert(0, value)
        self.__size += 1
    
    def pop(self):
        if self.__size == 0:
            raise StackIsEmptyException
        to_pop = self.__items[0]
        self.__items.pop(0) # O(k) https://www.google.com/search?q=python+pop+time+complexity&oq=python+pop+time+&aqs=chrome.1.69i57j0i19j0i19i22i30l8.5523j0j7&sourceid=chrome&ie=UTF-8
        self.__size -= 1
        return to_pop
    
    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0


s = Stack()

print(s.get_size())
print(s.is_empty())
# print(s.peek()) # Exception
s.push(1)
print(s.get_size())
print(s.is_empty())

s.push(2)
s.push(3)

print(" <TWO PUSH> ")

print(s)

s.pop()

print(" <POP> ")

print(s)




