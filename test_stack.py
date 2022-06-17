import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
    
    def testEmptyStack(self):
        self.assertTrue(self.stack.is_empty())
    
    def testEmptyStackException(self):
        with self.assertRaises(Exception):
            self.stack.pop()
    
    def testNotEmptyStack(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())
    
    def testPushStack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.size, 3)
    
    def testPopStack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        pop = self.stack.pop()
        pop = self.stack.pop()

        self.assertEqual(2, pop)