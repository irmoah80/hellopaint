import stack
from PyQt5.QtWidgets import QApplication

# impl ------------------------------------------

class UndoRedo:
    stack_main = None
    stack_cach = None

    def __init__(self) -> None:
        self.stack_main = stack.Stack()
        self.stack_cach = stack.Stack()

    def push(s , v):
        if not s.stack_cach.is_empty():
            s.c_cach()
        s.stack_main.push(v)
        print('push done')

    def clearall(s):
        s.stack_cach.clear()
        s.stack_main.clear()

    def c_main(s):
        s.prev_point = tuple()

    def c_cach(s):
        s.stack_cach.clear()

    def undo(s):
        if s.stack_main.size() == 1 :
            QApplication.beep()
            return s.stack_main.top()

        s.stack_cach.push(s.stack_main.pop())
        return s.stack_main.top()

    def redo(self):
        if self.stack_cach.is_empty() :
            QApplication.beep()
            return False

        self.stack_main.push(self.stack_cach.pop())
        return self.stack_main.top()

# tests ------------------------------------------

import unittest

class URTest(unittest.TestCase):
    def test_push(self):
        ur = UndoRedo()
        ur.push(1)
        ur.push(2)
        ur.push(3)
        ur.push(4)

        self.assertEqual(ur.stack_main.array, [1 , 2, 3, 4])

    def test_undo(self):
        ur = UndoRedo()
        ur.push(1)
        ur.push(2)
        ur.push(3)
        ur.push(4)
        
        ur.undo()
        ur.undo()

        self.assertEqual(ur.stack_main.array, [1 , 2])
        self.assertEqual(ur.stack_cach.array, [4, 3])

    def test_undo_redo(self):
        ur = UndoRedo()
        ur.push(1)
        ur.push(2)
        ur.push(3)
        ur.push(4)
        
        ur.undo()
        ur.undo()

        ur.redo()

        self.assertEqual(ur.stack_main.array, [1 , 2, 3])
        self.assertEqual(ur.stack_cach.array, [4])
    
    def test_undo_redo_push(self):
        ur = UndoRedo()
        ur.push(1)
        ur.push(2)
        ur.push(3)
        ur.push(4)
        
        ur.undo()
        ur.undo()

        ur.redo()

        ur.push(5)

        self.assertEqual(ur.stack_main.array, [1 , 2, 3, 5])
        self.assertEqual(ur.stack_cach.array, [])

    def test_change_line(s):
        ur = UndoRedo()
        ur.push(1)
        ur.push(2)
        ur.push(3)
        ur.push(4)

        ur.undo()
        ur.undo()
        ur.undo()

        ur.push(5)
        ur.push(6)
        ur.push(7)

        ur.undo()
        ur.redo()
        s.assertEqual(ur.stack_main.array, [1 , 5, 6, 7])
        s.assertEqual(ur.stack_cach.array, [])



# t = URTest()
# t.test_push()
# t.test_undo()
# t.test_undo_redo()
# t.test_undo_redo_push()
# t.test_change_line()
