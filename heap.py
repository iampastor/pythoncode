#coding:utf-8

from random import randint
from heapq import *

def heap_sort(iterable):
	lst = []
	for x in iterable:
		heappush(lst,x)
	lst = [heappop(lst) for i in range(len(lst))]
	return lst
def merge_sort(iterable):
	if len(iterable) <= 1:
		return iterable
	else:
		mid = len(iterable) / 2
		left = merge_sort(iterable[:mid])
		right = merge_sort(iterable[mid:])
		return list(merge(left,right))
if __name__ == "__main__":
	lst = [randint(0,100) for x in range(11)]
	print heap_sort(lst)
	print merge_sort(lst)