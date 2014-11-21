class Parent:
  c = 0
  def __init__(self):
    self.a = 10
    self.b = 11
    Parent.c += 1

 
  def getCount(self):
    print Parent.c

  def increase(self):
    self.a += 1
    self.b += 1
  def printval(self):
    print self.a,self.b
p = Parent()
p2 = Parent()
p.getCount()
p2.getCount()
p.increase()
p2.increase()
p.printval()
p2.printval()
