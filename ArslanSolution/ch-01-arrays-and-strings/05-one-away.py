# Determine whether the edit distance between two strings is less than 2.

def one_away(str1, str2):
  if (len(str1)==len(str2)):
    return edit_replace(str1,str2)
  elif (len(str1)==len(str2)+1):
    return edit_insert_remove(str1,str2)
  elif (len(str1)+1==len(str2)):
    return edit_insert_remove(str2,str1)  
  else:
    return False

def edit_replace(str1,str2):
  check=0
  for s1,s2 in zip(str1,str2):
    if(s1 != s2):
      check += 1
    if (check >1):
      return False
  return True

def edit_insert_remove(str1,str2):
  check=0
  index1=0
  index2=0
  while index2 < len(str2):
    if(check > 1):
      return False
    if(str1[index1] != str2[index2]):
      index1 += 1
      check += 1
    if(str1[index1] == str2[index2]):
      index1 += 1
      index2 += 1
  return True

    

if __name__ == "__main__":
  import sys
  print(one_away(sys.argv[-2], sys.argv[-1]))
