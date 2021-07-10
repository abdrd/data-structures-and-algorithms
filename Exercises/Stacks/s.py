class StackIsEmptyException(Exception):
    pass

"""
                      TOP  
                       |
                       v 
    [  [w]  [z]  [y]  [x]  ]
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
        to_return = self.__items[-1]
        return to_return
    
    def push(self, value):
        self.__items.append(value)
        self.__size += 1
    
    def pop(self):
        if self.__size == 0:
            raise StackIsEmptyException
        to_pop = self.__items[-1]
        self.__items.pop()
        self.__size -= 1
        return to_pop
    
    def get_size(self):
        return self.__size
    
    def is_empty(self):
        return self.__size == 0
    
    def items(self):
        return self.__items