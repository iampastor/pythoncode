from functools import wraps
def hello(func):
	def wrap():
		print "hello",func.__name__
		func()
		print "goodbye",func.__name__
	return wrap

@hello
def foo():
	print "i am foo"

def makeHtmlTag(tag,*args,**kwargs):
	def real_wraper(func):
		css_class = " class=%s"%(kwargs.get("css","")) if "css" in kwargs else ""
		@wraps(func)
		def wraper():
			return "<" +tag + css_class + ">" + func(*args,**kwargs) + "</" + tag + ">"
		return wraper
	return real_wraper

@makeHtmlTag("p",css="blod")
def saysomething(*args,**kwargs):
	return "this is say something"


def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a),
                  fns,
                  data)

class Student(object):
	@property
	def name(self):
		return self._name
	@name.setter
	def name(self,value):
		if len(value) > 5:
			raise ValueError("name length must less than 5")
		self._name = value
	@name.deleter
	def name(self):
		del self._name

if __name__ == "__main__":
	#print saysomething()
	student = Student()
	student.name = "yangx"
	print student.name
