import re
import requests
from multiprocessing import Pool

def request(url):
	resp = None
	try:
		resp = requests.get(url,timeout=10)

	except Exception:
		pass
	return resp
def get_urls(url):
	pattern = r"http:\/\/[\w_%\&\?\.\/]+"

	resp = request(url)
	if resp:
		txt = resp.text
	else:
		txt = ""
	return re.findall(pattern,txt)
if __name__ == '__main__':
	p = Pool(100)
	urls = get_urls("http://www.163.com")
	p.map(request,urls)
	

	

