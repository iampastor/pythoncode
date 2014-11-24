#encoding=utf-8
from PIL import Image
import argparse
import os,os.path
import sys

def thumb(src,to):
	"""
	读取文件或者遍历文件夹，将图片缩略
	"""
	if not os.path.exists(src):
		print "src directory or file not exits"
		sys.exit(0)
	if os.path.isfile(src):
		thumb_file(src,to)
	elif os.path.isdir(src):
		thumb_dir(src,to)
	else:
		print "src neither a file or a directory"
		sys.exit(0)

def thumb_file(src,to):
	#print src,to
	#print to + "/thumb_" + os.path.split(src)[1]
	img = Image.open(src)
	size = get_proper_size(img)
	img.thumbnail(size)
	if not os.path.exists(to):
		os.makedirs(to)
	img.save(to+"/thumb_"+os.path.split(src)[1])
	img.close()

def thumb_dir(src_dir,to_dir):
	for root,dirs,files in os.walk(src_dir,topdown=True):
		for fname in files:
			filename = os.path.join(root,fname)
			thumb_file(filename,to_dir)

def get_proper_size(fp,max_size=1000):
	"""
	获得图片一个合适的缩略大小，最大尺寸不要超过1000
	"""
	(width,height) = fp.size
	x = max(width,height) / max_size
	if x:
		return (width / x,height / x)
	return (width,height)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("src",default="full",help="file or directory  thumbnail from")
	parser.add_argument("to",default="thumb",help="directory thumbnail to")
	args = parser.parse_args()
	thumb(args.src,args.to)

if __name__ == "__main__":
	main()

