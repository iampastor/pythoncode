from bs4 import BeautifulSoup
import urllib
import urllib2
import os,os.path
import socket
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
num = 4634
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"

for i in range(1):
	num += 1
	url = "http://www.meizitu.com/a/"+str(num)+".html"
	request = urllib2.Request(url)
	request.add_header("User-Agent",user_agent)
	opener = urllib2.build_opener()
	conn = opener.open(request)
	data = conn.read()#.decode("gbk").encode("utf-8")
	soup = BeautifulSoup(data)
	print soup.prettify()
	imgs = soup.select(".postContent img")
	strnum = str(num)
	os.mkdir(strnum)
	for img in imgs:
		imgurl = img["src"]
		try:
			req = urllib2.Request(imgurl)
			req.add_header("User-Agent",user_agent)
			con = urllib2.urlopen(req,timeout=600)
			f = open(strnum + "/"+imgurl.split("/")[-1],"wb")
			f.write(con.read())			
		except socket.error:
			pass
		finally:
			f.close()
			con.close()
	conn.close()