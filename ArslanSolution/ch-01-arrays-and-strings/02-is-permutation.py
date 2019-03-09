# Determine whether or not one string is a permutation of another.

def is_permutation(str1, str2):
    if len(str1)!=len(str2):
        return False

    l1=list(str1)
    l2=list(str2)
    l1.sort()
    l2.sort()

    if (l1==l2):
        return True
    else:
        return False

if __name__ == "__main__":
  import sys
  print(is_permutation(sys.argv[-2], sys.argv[-1]))
