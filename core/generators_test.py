import unittest

from core.generators import SimpleGenerator


class GeneratorTest(unittest.TestCase):

    def test_simple_generator(self):
        simple_gen = SimpleGenerator()
        user = simple_gen.generate()
        self.assertTrue(user.firstname in SimpleGenerator.first_names)
        self.assertTrue(user.lastname in SimpleGenerator.last_names)
        self.assertTrue(SimpleGenerator.min_age <= user.age <= SimpleGenerator.max_age)


if __name__ == '__main__':
    unittest.main()