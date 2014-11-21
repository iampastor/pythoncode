import threading
import time

tickets = 100
lock = threading.RLock()	
def sell(index):
	global tickets
	while True:
		lock.acquire()
		if tickets > 0:
			tickets -= 1
			print "%s sell ticket %s"%(index,tickets)
			lock.release()
			time.sleep(0.1)
		else:
			lock.release()
			break

def main():
	threads = []
	for i in range(3):
		th = threading.Thread(target=sell,args=(i,))
		threads.append(th)

	for th in threads:
		th.start()
		#th.join()
if __name__ == "__main__":
	main()