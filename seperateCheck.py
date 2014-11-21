import re,collections
def words(text):return re.findall('[a-z]+',text.lower())
def trains(feature):
  model = collections.defaultdict(lambda:1)
  for f in feature:
    model[f] += 1
  return model
NWORDS = trains(words(file('big.txt').read()))
alphabet = "abcdefghijklmnopqrstuvwxyz"
def edits1(word):
  splits = [(word[:i],word[i:]) for i in range(len(word) + 1)]
  deletes = [a + b[1:] for a,b in splits if b]
  transposes = [a + b[1] + b[0] + b[2:] if for a,b in splits if len(b) > 1]
  replaces = [a + c + b[1:] for a,b in splits for c in alphabet if b]
  inserts = [a + c + b for a,b in splits for c in alphabet]
  return set(deletes + transposes + replaces + inserts)


  
