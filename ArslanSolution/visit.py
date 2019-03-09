# Determine whether or not a given string is a rotation of another string.

import unittest
from enum import Enum
import operator

def visit(s):
    class Dir(Enum):
        W = (-1,0)
        E = (1,0)
        N = (0,1)
        S = (0,-1)
    
    visited=[(0,0)]
    answer=0
    for l in s:
        if l=='W':
            tup1=Dir.W.value
        elif l=='E':
            tup1=Dir.E.value
        elif l=='N':
            tup1=Dir.N.value
        elif l=='S':
            tup1=Dir.S.value
        else:
            return 0

        tup2=tuple(map(operator.add, visited[-1], tup1))
        print(tup2)
        if tup2 in visited:
            answer=answer+1
        visited.append(tup2)


       
    return answer

        
  


class Test(unittest.TestCase):
  def test_is_rotation(self):
    s1 = "WEWNES"
    self.assertEqual(visit(s1),3)
    
  

if __name__ == "__main__":
    unittest.main()
