"""
Items are ordered in an ascending order.

HEAD
 |
 v
[1] <-> [4] <-> [16] <-> [25] <-> ...

"""

class Node:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: Node = None
        self.prev: Node = None
    

class OrderedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.size: int = 0
    """
    def items(self) -> list[int]:
        if self.size > 1:
            res = []
            cur = self.head
            res.append(cur)
            while cur.next:
                cur = cur.next
                res.append(cur)
            return res
        else:
            return []    
    """
    """
        Only going to implement the add and find methods, because other methods are 
        basically the same. 
    """
    def add(self, value: int):
        node_to_add = Node(value) 
        
        if self.size == 0:
            self.head = node_to_add
            self.size += 1

        else:   
            cur = self.head
            if self.head.value > value:
                temp = self.head
                self.head.prev = node_to_add
                self.head = node_to_add
                self.head.next = temp
                self.size += 1
            else:
                while cur.next:
                    cur = cur.next

                    if cur.value > value:
                        before_cur = cur.prev
                        cur.prev = node_to_add
                        node_to_add.next = cur
                        node_to_add.prev = before_cur
                        self.size += 1
                        return
                cur.next = node_to_add
                node_to_add.prev = cur
                self.size += 1

    # check whether a node with the given value exists in the list
    def exists(self, value: int) -> bool:
        if self.size == 0:
            return False
        
        cur = self.head
        while cur.next:
            if cur.value > value:
                return False
            if cur.value == value:
                return True
            cur = cur.next

        # last item
        return cur.value == value

l = OrderedList()
print(" <INIT> ")
print(l.head)

l.add(1)
print(" <ADD '1'> ")
print(l.head.value)

l.add(0)
print(" <ADD '0'> ")
print(l.head.value)
print(l.head.next.value)

l.add(3)
print(" <ADD '3'> ")
print(l.head.value)
print(l.head.next.value)
print(l.head.next.next.value)

l.add(5)
print(" <ADD '5'> ")
print(l.head.value)
print(l.head.next.value)
print(l.head.next.next.value)
print(l.head.next.next.next.value)

l.add(-2)
print(" <ADD '-2'> ")
print(l.head.value)
print(l.head.next.value)
print(l.head.next.next.value)
print(l.head.next.next.next.value)
print(l.head.next.next.next.next.value)


# I am starting to feel like an ancient Egyptian
print(l.exists(1))
print(l.exists(-2))
print(l.exists(0))
print(l.exists(3))
print(l.exists(5))
print(l.exists(2)) # false
print(l.exists(7)) # False
print(l.exists(119)) # False

