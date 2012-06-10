import os
import hello
import unittest
import tempfile

class HelloTestCase(unittest.TestCase):
    
    def test_getMetroEvents(self):
        r = hello.getMetroEvents('17835')
        self.assertEqual(r, 'hi')


if __name__ == '__main__':
    unittest.main()
