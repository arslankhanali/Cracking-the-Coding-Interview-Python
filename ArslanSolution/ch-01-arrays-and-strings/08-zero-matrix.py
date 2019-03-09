# Given a matrix, zero out every row and column that contains a zero.

import unittest
import copy 

def zero_out_row_col(m):
  len_row=len(m)
  len_col=len(m[0])

  n= copy.deepcopy(m)

  def zero_out(r,c):
    for i in range(len_row):
      for j in range(len_col):
        if(i==r or j==c):
          n[i][j]=0

  for row in range(len_row):
    for col in range(len_col):
      if (m[row][col]==0):
        zero_out(row,col)

  print(n)
  return n

class Test(unittest.TestCase):
  def test_zero_out_row_col_matrix(self):
    mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]] 
    self.assertEqual(zero_out_row_col(mat1), mat2)

if __name__ == "__main__":
  unittest.main()
