class Student:
  def __init__(self,name,age,score):
    self.name = name
    self.age = age
    self.score = score

def mycmp(s1,s2):
  if s1.score != s2.score:
    return cmp(s1.score,s2.score)
  elif s1.age != s2.age:
    return cmp(s1.age,s2.age)
  elif s1.name != s2.name:
    return cmp(s1.name,s2.name)
  else:
    return 1
def test():
  s1 = Student("abc",20,99)
  s2 = Student("bcd",19,97)
  s3 = Student("bed",20,97)
  stds = [s1,s2,s3]
  stds = sorted(stds,cmp=mycmp)
  for s in stds:
    print s.name,s.age,s.score
if __name__ == "__main__":
  test()
