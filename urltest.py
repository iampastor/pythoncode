import urllib2
import base64
req = urllib2.Request("http://192.168.1.1")
psw_dict = {"root":"root","admin":"admin","bounce":"6231666"}
for k,v in psw_dict.iteritems():
    base64_str = base64.b64encode(k+":"+v)
    header = {"Authorization":"Basic " + base64_str}
    req.add_header("Authorization","Basic " + base64_str)
    try:
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print 'error'
    else:
        print "right"
