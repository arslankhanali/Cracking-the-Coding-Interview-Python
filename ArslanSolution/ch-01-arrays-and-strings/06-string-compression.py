# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.

def compress(string):
  string= string +'x' 
  current_letter=string[0]
  s=""
  count=0

  for i in range(len(string)):
    if (current_letter==string[i]):
      count +=1
    else:
      s+=current_letter+ str(count)
      current_letter= string[i]
      count=1

    

  if len(s) < len(string):
    return s
  else:
    return string
   


if __name__ == "__main__":
  import sys
  print(compress(sys.argv[-1]))
