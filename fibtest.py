#coding:utf-8

def fib2(n):
	result = [0,1]
	for x in range(2,n):
		result.append(result[x - 1] + result[x - 2])
	return result

if __name__ == "__main__":
	print fib2(100)