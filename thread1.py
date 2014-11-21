import thread
import time
import random
tickets = 100
lock = thread.allocate_lock()
def sell(index):
	global tickets
	
	while True:
		lock.acquire()
		if tickets > 0:
			tickets -= 1
			print "%s sell  ticket %s"%(index,tickets)
		time.sleep(random.random())
		#lock.release()
def thread1():
	lock.acquire()
	time.sleep(2)
	print lock.locked()
def main():
	# idents = []
	# for i in range(3):
	# 	ident = thread.start_new_thread(sell,(i,))
	# 	idents.append(ident)
	# time.sleep(25)

	ident = thread.start_new_thread(thread1,())
	#lock.acquire()
	print lock.locked()
	time.sleep(1)
	lock.release()
	time.sleep(2)

if __name__ == "__main__":
	main()