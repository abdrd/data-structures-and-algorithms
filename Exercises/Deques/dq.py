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