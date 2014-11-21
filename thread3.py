import threading
import time

class Producer(threading.Thread):
	def __init__(self,t_name):
		threading.Thread.__init__(self,name=t_name)
	def run(self):
		global x
		while True:
			condition.acquire()
			if x > 0:
				condition.wait()
			else:
				for i in range(5):
					x += 1
					print "produce %s"%(x)
				condition.notify()
			condition.release()
			time.sleep(0.2)
class Customer(threading.Thread):
	def __init__(self,t_name):
		threading.Thread.__init__(self,name=t_name)
	def run(self):
		global x
		while True:
			condition.acquire()
			if x <= 0:
				condition.wait()
			else:
				for i in range(5):
					x -= 1
					print "custome %s"%(x)
				condition.notify()
			condition.release()
			time.sleep(0.1)
x = 0
condition = threading.Condition()
def main():
	
	producer = Producer("producer")
	customer = Customer("customer")
	producer.start()
	print "start producer"
	customer.start()
	print "start customer"

if __name__ == "__main__":
	main()