import unittest
import matiscapy

class TestMatiscapy(unittest.TestCase):
	def setUp(self):
		self.url = "http://www.sina.com.n"
		#self.num = 1
		#self.user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"
	def test_download(self):
		data = matiscapy.download(self.url)
		self.assertEqual(data,'')
if __name__ == "__main__":
	unittest.main()