# Determine whether or not a string is a permutation of a palindrome,
# ignoring spaces.

def is_palindrome_permutation(string):
  letter_count=Counter()

  for letter in string.replace(" ",""):
    letter_count[letter] += 1

  print(letter_count)

  total_odd=0
  for value in letter_count.values():
    if value%2 > 0:
      total_odd +=1

  if total_odd > 1:
    return False
  else:
    return True

class Counter(dict):
  def __missing__ (self,key):
    return 0 

if __name__ == "__main__":
  import sys
  print(is_palindrome_permutation(sys.argv[-1]))

