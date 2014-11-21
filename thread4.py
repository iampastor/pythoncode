import threading
import time
import Queue
class Producer(threading.Thread):
	def __init__(self,t_name):
		threading.Thread.__init__(self,name=t_name)
	def run(self):
		for count in range(10):
			queue.put(count)
			print "prodece %s"%(count)
			time.sleep(0.1)
class Customer(threading.Thread):
	def __init__(self,t_name):
		threading.Thread.__init__(self,name=t_name)
	def run(self):
		for x in range(10):
			count = queue.get()
			print "custome %s"%(count)
			time.sleep(0.2)
queue = Queue.Queue()
def main():
	
	producer = Producer("producer")
	customer = Customer("customer")
	producer.start()
	print "start producer"
	customer.start()
	print "start customer"

if __name__ == "__main__":
	main()