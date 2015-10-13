from main import PMi

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(3,PMi.at([]))


if __name__ == '__main__':
    unittest.main()
