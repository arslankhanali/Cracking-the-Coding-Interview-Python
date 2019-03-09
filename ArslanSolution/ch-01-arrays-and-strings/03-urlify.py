# Replace spaces in the middle of a string with "%20" assuming the end of the 
# string contains twice as many spaces as are in the middle.

def escape_spaces_1(string):
    return string.replace(" ",'%20')
  

if __name__ == "__main__":
  import sys
  print(escape_spaces_1(sys.argv[-1]))

