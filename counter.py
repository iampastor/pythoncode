#coding:utf-8
from collections import Counter
def most_char(string):
	counter = Counter(string)
	return counter.most_common(1)

def most_char2(string):
	result = {}
	for c in string:
		if c in result:
			result[c] += 1
		else:
			result[c] = 1
	
if __name__ == "__main__":
	print most_char2("ddddsdfisdfjsdfkloisdiof")