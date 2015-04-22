from __future__ import division
import pcap
import time
import threading
import signal
import sys
from dpkt import ethernet,ip,tcp,udp

total_len = 0

def print_ip(ip):
	print "%s.%s.%s.%s"%(ord(ip.src[0]),ord(ip.src[1]),ord(ip.src[2]),ord(ip.src[3])),
	print "->",
	print "%s.%s.%s.%s"%(ord(ip.dst[0]),ord(ip.dst[1]),ord(ip.dst[2]),ord(ip.dst[3])),

def calc_speed():
	while True:
		last = total_len
		time.sleep(1)
		now = total_len
		delta = now - last
		if delta > 2**20:
			print "%sM/s"%(delta / (2**20) )
		elif delta > 2**10:
			print "%sKB/s"%(delta / (2**10))
		else:
			print "%sB/s"%(delta)

def exit_handler(signum, frame):
	print "exit now..............."
	sys.exit(-1)

def pcap_handler(ts,data,*arg):
	# eth = ethernet.Ethernet(data)
	# ip = eth.data
	print "catch..."
	global total_len
	total_len += len(data)

def main():

	devs = pcap.findalldevs()
	print "please chose which interface to listen:"
	for index,dev in enumerate(devs):
		print str(index)+":"+dev
	i = raw_input()
	dev = devs[int(i)]
	pc = pcap.pcap(dev)
	print "listening on %s"%pc.name

	# th = threading.Thread(target=calc_speed)
	# th.start()
	pc.loop(-1,pcap_handler)
		


if __name__ == '__main__':
	#signal.signal(signal.SIGINT,exit_handler)
	main()
	
