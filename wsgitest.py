from wsgiref.simple_server import make_server
from application import application

httpd = make_server("",8888,application)
print "start http server at port 8888"
httpd.serve_forever()