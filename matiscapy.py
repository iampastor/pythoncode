#coding=utf-8
import threading
from Queue import Queue
from bs4 import BeautifulSoup
import urllib
import urllib2
import os,os.path
import socket
import sys
import gzip
import StringIO
reload(sys)
sys.setdefaultencoding("utf-8")

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"

def download(url):
	'''
	下载url指定的页面，对gzip进行解压处理
	返回读取的数据,可能返回为空字符

	'''
	request = urllib2.Request(url)
	request.add_header("User-Agent",user_agent)
	opener = urllib2.build_opener()
	try:
		conn = opener.open(request,timeout=60)
		headers = conn.info()
		data = conn.read()
		if "content-encoding" in headers:
			encoding = headers["content-encoding"]
			if encoding.lower() == "gzip":
				data = gzip.GzipFile(fileobj=StringIO.StringIO(data)).read()
	except urllib2.URLError,e:
			print e.reason,url
	else:
		conn.close()
		return data
	return ""
def extract(data,selector):
	'''提取页面中的指定内容，通过selector来选择
	selector的格式同css选择器类似
	'''
	soup = BeautifulSoup(data)
	imgs = soup.select(selector)#".postContent img"
	
	imgurl = [img["src"] for img in imgs]
	return imgurl
def retrive_pic(picurl,path="./"):
	'''下载图片，放在path指定的目录中，
	如果path未指定，默认为当前目录，并
	提取图片的名字作为保存的名字
	'''
	#if not os.path.exists(path):
	#	os.makedirs(path)
	try:
		req = urllib2.Request(picurl)
		req.add_header("User-Agent",user_agent)
		con = urllib2.urlopen(req,timeout=60)
		try:
			f = open(path+picurl.split("/")[-1],"wb")
			bs = 1024*8
			read = 0
			while True:
				block = con.read(bs)
				if block == "":
					break
				read += len(block)
				f.write(block)
		except IOError,e:
			print e
		else:
			f.close()			
		#print "downloading file %s"%(path+picurl.split("/")[-1])
	except urllib2.URLError,e:
		print e.reason,picurl
	else:		
		con.close()

def extract2queue(url,selector,queue):
	data = download(url)
	imgurls = extract(data,selector)
	[queue.put(imgurl) for imgurl in imgurls]
	#print "extract url %s"%url

def retrice_from_queue(queue,path="./"):
	global count
	global lock
	lock.acquire()
	tmp = count
	count += 1
	lock.release()
	picurl = queue.get()
	retrive_pic(picurl,path+"/"+str(tmp)+"-")
class Extractor(threading.Thread):
	'''下载页面，提取其中的内容，放到Queue中，供下载图片使用
	'''
	def __init__(self,queue,url,sta,end):
		threading.Thread.__init__(self)
		self.data = queue
		self.url = url
		self.sta = sta
		self.end = end
	def run(self):
		while self.sta <= self.end:
			tmpurl = self.url + str(self.sta)+ ".html"
			extract2queue(tmpurl,".postContent img",self.data)
			self.sta += 1
		global extract_finished
		extract_finished = True
		print "extractor exit"
class Retriver(threading.Thread):
	'''提取队列中的图片的URL，下载到相应的目录
	'''
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.data = queue
	def run(self):
		global extract_finished
		while not extract_finished or not self.data.empty():
			retrice_from_queue(self.data,"imgs")
		print "Retriver" + self.name + "exit"
lock = threading.RLock()
count = 1
extract_finished = False
def main():
	url = "http://www.meizitu.com/a/"
	# num = 4097
	imgQueue = Queue()
	# data = download(url+str(num)+".html")
	# imgs = extract(data,".postContent img")
	# for img in imgs:
	# 	retrive_pic(img,"imgs/"+str(num))
	sta,end = 31,40
	#1-750,3550-4634
	global count
	count = 8241
	ex1 = Extractor(imgQueue,url,4634,4635)
	#ex2 = Extractor(imgQueue,url,3550,4100)
	#ex3 = Extractor(imgQueue,url,4101,4635)
	ex1.start()
	#ex2.start()
	#ex3.start()
	retrs = []
	for i in range(10):
		retr = Retriver(imgQueue)
		retrs.append(retr)
		retr.start()
if __name__ == "__main__":
	main()