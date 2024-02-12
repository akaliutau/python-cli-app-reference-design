import unittest

from core.model import User


class UserTest(unittest.TestCase):

    def test_user(self):
        user = User('Alice', 'Amsterdam', 29)
        self.assertEqual('Alice', user.firstname)
        self.assertEqual('Amsterdam', user.lastname)
        self.assertEqual(29, user.age)


if __name__ == '__main__':
    unittest.main()
