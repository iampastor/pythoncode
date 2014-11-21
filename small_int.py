#coding:utf-8
def small_int(num):
	lst = [i for i in str(num) if i != '0']
	lst.sort()
	n0 = len(str(num)) - len(lst)
	lst.insert(1,'0'*n0)
	return "".join(lst)

if __name__ == "__main__":
	print small_int(123970051255723123901234)