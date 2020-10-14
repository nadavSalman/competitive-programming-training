from question2.solution import str_prefix
import unittest


class TestStrPrefix(unittest.TestCase):

  def test_in_str_boundry(self):
      self.assertEqual(str_prefix('aabb',2), 'aa')


if __name__ == '__main__':
    unittest.main()