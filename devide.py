#coding:utf-8

def devide(x,y,limit = None):
	result = ""
	result += str(x / y)
	r = x % y
	result += '.'
	r_list = [r]
	cycle = None
	while limit:
		x = r * 10
		result += str(x / y)
		r = x % y

		limit -= 1

		if r in r_list:
			cycle = result[result.index('.') + 1:][r_list.index(r):]
			break
		r_list.append(r)

	return result,cycle

if __name__ == "__main__":
	result,cycle = devide(8,7,10)
	print result,cycle