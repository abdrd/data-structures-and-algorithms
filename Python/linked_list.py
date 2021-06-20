class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Node = None

class LinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def length(self) -> int:
        counter = 0
        cur = self.head

        if self.head:
            counter += 1
            
            while cur.next:
                cur = cur.next
                counter += 1
        return counter

    def append(self, new_element: Node) -> None:
        cur = self.head
        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = new_element
        else:   
            self.head = new_element
    
    def value_at(self, index: int):
        cur = self.head
        idx = 0

        if cur:
            if index == idx:
                return cur.value

            while cur.next:
                cur = cur.next
                idx += 1
                
                if index == idx:
                    return cur.value
                
        return None      

    def node_at(self, index: int):
        cur = self.head
        idx = 0

        if cur:
            if index == idx:
                return cur

            while cur.next:
                cur = cur.next
                idx += 1
                
                if index == idx:
                    return cur
                
        return None     

    def insert_at(self, index: int, new_node: Node):
        cur = self.head
        idx = 0

        if index == 0:
            new_node.next = self.head
            self.head = new_node

        if self.head:
            while cur:
                cur = cur.next
                idx += 1
                
                if index == idx:
                    node_before_cur = self.node_at(idx - 1)
                    node_before_cur.next = new_node
                    new_node.next = cur

    
    def delete(self, value):
        cur = self.head
        idx = 0

        if value == cur.value:
            second_node = self.node_at(1)
            self.head = second_node
            cur.next = None

        while cur.next:
            cur = cur.next
            idx += 1
            
            if value == cur.value:
                prev_node = self.node_at(idx - 1)
                try:
                    next_node = self.node_at(idx + 1)
                    prev_node.next = next_node
                    cur.next = None
                except:
                    prev_node.next = None
    
    def update(self, index, new_value):
        node_to_update = self.node_at(index)
        
        try:
            node_to_update.value = new_value
        except:
            raise TypeError

l = LinkedList()

print("LENGTH OF LIST: ", l.length())

n1 = Node("FIRST NODE")
l.append(n1)

print("LENGTH OF LIST: ", l.length())


n2 = Node("SECOND NODE")
l.append(n2)

print("LENGTH OF LIST: ", l.length())


n3 = Node("THIRD NODE")
l.append(n3)

n4 = Node("FOURTH NODE")
l.append(n4)

n5 = Node("INSERT THIS")
l.insert_at(2, n5)

n6 = Node("I AM TOP")
l.insert_at(0, n6)

n7 = Node("I AM LAST")
l.insert_at(6, n7)

n8 = Node("NO, I AM THE LAST")
l.insert_at(7, n8)

print("LENGTH OF LIST: ", l.length())


"""
    0 - I AM TOP
    1 - FIRST NODE
    2 ...
    6 - FOURTH NODE
"""

print(l.value_at(0))
print(l.value_at(1))
print(l.value_at(2))
print(l.value_at(3))
print(l.value_at(4))
print(l.value_at(5))
print(l.value_at(6))
print(l.value_at(7))


l.delete("FIRST NODE")
l.delete("FOURTH NODE")

print(" <DELETED SOME> ")

print(l.value_at(0))
print(l.value_at(1))
print(l.value_at(2))
print(l.value_at(3))
print(l.value_at(4))
print(l.value_at(5))
print(l.value_at(6))
print(l.value_at(7))

print("LENGTH OF LIST: ", l.length())

print(" <UPDATED SOME> ")

l.update(0, "UPDATED_ TOP NODE")
l.update(1, "UPDATED BLA BLA")
l.update(l.length() - 1, "UPDATED LAST NODE")
#l.update(8, "ERROR")

print(l.value_at(0))
print(l.value_at(1))
print(l.value_at(2))
print(l.value_at(3))
print(l.value_at(4))
print(l.value_at(5))
