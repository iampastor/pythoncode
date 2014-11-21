#coding:utf-8

def del_space(string):
	split_string = string.split(" ")
	str_list = [s for s in split_string if s != ""]
	return " ".join(str_list)

if __name__ == "__main__":
	string = " hello, my name   is   pastor ,oh!"
	print del_space(string)