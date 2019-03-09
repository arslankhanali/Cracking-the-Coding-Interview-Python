# Rotate a square matrix by 90 degrees counter-clockwise about its center.

# TODO Use a matrix instead of a two-dimensional list.

import unittest

def rotate_matrix(m):
  m_rot=[]
  for i in range(len(m)):
    row=[]
    for j in range(len(m)):
      row.append(m[j][i])
    m_rot.insert(0,row)
  return m_rot


class Test(unittest.TestCase):
  def test_rotate_matrix(self):
    mat1 = [[1,2],[3,4]]
    mat2 = [[2,4],[1,3]]
    self.assertEqual(rotate_matrix(mat1), mat2)
    mat3 = [[1,2,3],[4,5,6],[7,8,9]]
    mat4 = [[3,6,9],[2,5,8],[1,4,7]]
    self.assertEqual(rotate_matrix(mat3), mat4)
    mat5 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    mat6 = [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]
    self.assertEqual(rotate_matrix(mat5), mat6)
  
if __name__ == "__main__":
  unittest.main()
