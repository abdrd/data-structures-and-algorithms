class StackIsEmptyException(Exception):
    pass

#          TOP
#           |
#           v
# [1, 2, 3, 4]

"""
In this version of the implementation, I am assuming the top of the stack is the end of the list. 

This version's pop and insert (append) operations will take O(1) time; because using pop and insert
methods without any index argument takes O(1) time while calling them with index arguments
takes O(n) time (n stands for the number of elements in the list), because Python has to 
rearrange all the items in the list. 
"""

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
        self.__items.append(value)
        self.__size += 1
    
    def pop(self):
        if self.__size == 0:
            raise StackIsEmptyException
        to_pop = self.__items[0]
        self.__items.pop()
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




