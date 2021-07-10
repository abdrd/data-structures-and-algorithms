"""
Simulate a hot-potato game
https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimulationHotPotato.html
"""
from q import Queue, Node

KIDDOS = ["Ali", "Veli", "Elif", "Hasan", "Tuğçe" "Mehmet", "Ayşe", "Burak", "Meryem"]

def hot_potato(num=len(KIDDOS), kids: list[str] = KIDDOS) -> str:
    winner = None
    qu = Queue()

    for kid in kids:
        qu.enqueue(Node(kid))

    while qu.size > 1:
        for i in range(num):
            front_kid = qu.peek()
            qu.dequeue()
            qu.enqueue(front_kid)
        qu.dequeue()

    winner = qu.peek()
    return winner.value


print(hot_potato(5))
print(hot_potato(3))
print(hot_potato(2))
print(hot_potato(4))