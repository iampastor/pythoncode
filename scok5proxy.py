import socks
import socket
import urllib2
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
#socket.socket = socks.socksocket

httpHandler = urllib2.HTTPHandler(1)
httpsHandler = urllib2.HTTPSHandler(1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
data =  urllib2.urlopen('http://www.python.org',timeout=10).read()#.decode("gbk").encode("utf-8")
f = open("138.html","wb")
f.write(data)
f.close()