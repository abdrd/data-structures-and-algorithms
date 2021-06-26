package main

import (
	"fmt"
	"log"
)

/*
* Stack implementation in Golang.
* (using doubly linked list)
 */

type Node struct {
	Value interface{}
	Above *Node
	Below *Node
}


// TODO implement stack in go


type Stack struct {
	Top *Node
	Size int
}

func (s *Stack) Push(n *Node) {
	if s.Size == 0 {
		s.Top = n
		s.Size++
	} else {
		top := s.Top
		n.Below = s.Top
		top.Above = n
		s.Top = n
		s.Size++
	}
}

func (s *Stack) Pop() *Node {
	if s.Size == 0 {
		// dont bother with returning errors
		log.Fatalln("stack is empty")
	} else if s.Size == 1 {
		s.Top = nil
		s.Size--
	} 

	toPop := s.Top
	s.Top = toPop.Below
	fmt.Println(toPop.Below)
	toPop.Below = nil
	return toPop
}

func main() {
	var s Stack

	fmt.Println(s)

	n1 := Node{Value: "FIRST_NODE"}
	s.Push(&n1)

	fmt.Println(s.Top.Value, s.Size)

	n2 := Node{Value: "SECOND_NODE"}
	s.Push(&n2)

	fmt.Println(s.Top.Value, s.Size)
	
	fmt.Println(/*s.Top.Below.Value,*/ s.Top.Above.Value)

	popped := s.Pop()
	fmt.Println(popped.Value)

	fmt.Println(s.Top.Value)
}