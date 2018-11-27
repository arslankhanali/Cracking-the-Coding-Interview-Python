# Determine whether or not a given string is a rotation of another string.

import unittest

def is_rotation(s1, s2):
  s1=s1+s1

  if s2 in s1:
    return True
  else:
    return False


class Test(unittest.TestCase):
  def test_is_rotation(self):
    s1 = "tabletop"
    s2 = "toptable"
    s3 = "optalbet"
    self.assertTrue(is_rotation(s1, s2))
    self.assertFalse(is_rotation(s1, s3))
  

if __name__ == "__main__":
  unittest.main()
