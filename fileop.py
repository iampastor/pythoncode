import os
def writeFile(f):
  line = ""
  while line != ".":
    line = raw_input()
    f.write(line + os.linesep)

def readFile(f):
  for s in f:
    print s,

def main():
  while True:
    try:
      fname = raw_input("enter a file name:")
      op = raw_input("read or write?(r/w)")
      f = open(fname,op)
      break
    except IOError,e:
      print "file error:", e
  if op == "w":
    print "enter some words,enter '.' to end"
    writeFile(f)
  elif op == "r":
    readFile(f)
  else:
    print "wrong operation"
  f.close()
  print "Done"
if __name__=="__main__":
  main()
