#coding:utf-8
from random import randint
from bisect import *
def binary_search(lst,value,low,high):
	if low > high:
		return -1
	mid = (low + high) / 2
	if value == lst[mid]:
		return mid
	elif value < lst[mid]:
		return binary_search(lst,value,low,mid - 1)
	else:
		return binary_search(lst,value,mid + 1,high)
def binary_search1(lst,value):
	low,high = 0,len(lst) - 1
	while low <= high:
		mid = (low + high) / 2
		if lst[mid] == value:
			return mid
		elif lst[mid] < value:
			low = mid + 1
		else:
			high = mid - 1
	return -1	

def binary_search2(lst,value):
	i = bisect_left(lst,value)
	if i != len(lst) and lst[i] == value:
		return i
	return -1	


if __name__ == "__main__":
	lst = [randint(0,100) for i in range(10)]
	lst.sort()
	print lst
	# print binary_search(lst,80,0,len(lst) - 1)
	print binary_search2(lst,80)