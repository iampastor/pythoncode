class MyMetaClass(type):
	def __new__(cls,name,bases,attrs):
		print "meta class called"
		print cls,name,bases,attrs

class Foo(object):
	__metaclass__ = MyMetaClass
	name = "yangxin"
	age = "23"
