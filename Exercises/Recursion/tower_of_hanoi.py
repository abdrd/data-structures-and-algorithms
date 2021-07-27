# https://stackoverflow.com/questions/19217565/understanding-double-recursion

def move(from_peg, to_peg):
    print(f"{from_peg} \t--> {to_peg}")

def hanoi(number_of_disks, from_peg, to_peg, auxiliary_peg):
    if number_of_disks == 0:
        return
    hanoi(number_of_disks - 1, from_peg, auxiliary_peg, to_peg)
    move(from_peg, to_peg)
    hanoi(number_of_disks - 1, auxiliary_peg, to_peg, from_peg)


#hanoi(4, "A", "C", "B")
hanoi(10, "START", "AUX", "TARGET")