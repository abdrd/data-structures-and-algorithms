import unittest
from .. import linked_list

class TestLinkedList(unittest.TestCase):
    def __init__(self): 
        self.l = linked_list.LinkedList()

    def test_append(self):
        length_before = self.l.length
        self.l.append("APPENDED")
        self.assertEqual(length_before + 1, self.l.length, "couldnt append")

if __name__ == '__main__':
    unittest.main()