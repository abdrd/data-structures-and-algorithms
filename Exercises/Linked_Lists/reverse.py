from l import DoublyLinkedList, Node

"""
    given a linked list like this:
    
    HEAD
    |
    v
    1 <-> 2 <-> 3 <-> 4 <-> 5 -> NULL

    we want reverse_linked_list function to turn it to this:

                                   HEAD
                                    |
                                    v
    NULL <- 1 <-> 2 <-> 3 <-> 4 <-> 5

            OR to this:

    HEAD
     |
     v
     5 <-> 4 <-> 3 <-> 2 <-> 1 -> NULL 

"""
def reverse_linked_list(llist: DoublyLinkedList) -> DoublyLinkedList:
    if llist.size == 0:
        raise Exception("list is empty")

    if llist.size == 1:
        return llist
    
    temp = None
    cur = llist.head

    while cur: 
        # this is None at the beginning
        temp = cur.prev
        cur.prev = cur.next
        cur.next = temp
        cur = cur.prev

    return llist

"""TEST"""

l1 = DoublyLinkedList()

#reverse_linked_list(l1) # raised an Exception

n1 = Node(1)
l1.prepend(n1)


n2 = Node(2)
l1.prepend(n2)

n3 = Node(3)
l1.prepend(n3)

print("HEAD: ", reverse_linked_list(l1).head.value)
print("HEAD PREV: ", reverse_linked_list(l1).head.prev)

print("HEAD NEXT: ", reverse_linked_list(l1).head.next.value)
print("HEAD NEXT PREV: ", reverse_linked_list(l1).head.next.prev.value)


"""
print("HEAD NEXT NEXT: ", reverse_linked_list(l1).head.next.next.value)
print("HEAD NEXT NEXT PREV: ", reverse_linked_list(l1).head.next.next.prev.value)
"""

