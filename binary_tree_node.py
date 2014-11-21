#coding:utf-8

class BinaryNode:
	"""
	binary tree node 
	"""
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self,data):
		if data > self.data:
			if self.right == None:
				self.right = BinaryNode(data)
			else:
				self.left.insert(data)
		elif data < self.data:
			if self.left == None:
				self.left = BinaryNode(data)
			else:
				self.left.insert(data)

	def insert1(self,data):
		ptr = self
		prev = ptr
		while ptr != None:
			if data > ptr.data and ptr.right is None:
				ptr.right = BinaryNode(data)
				break
			elif data > ptr.data and ptr.right is not None:
				ptr = ptr.right
			elif data < ptr.data and ptr.left is None:
				ptr.left = BinaryNode(data)
				break
			elif data < ptr.data and ptr.left is not None:
				ptr = ptr.left

	def travese(self,root):
		if root:
			self.travese(root.left)
			print root.data
			self.travese(root.right)

	def look_up(self,data):
		if self is None:
			return None
		if self.data == data:
			return self
		elif self.data > data:
			return self.left.look_up(data)
		elif self.data < data:
			return self.right.look_up(data)

	def preorder(self):
		stack = []
		ptr = self
		while ptr != None or len(stack) != 0:
			while ptr != None:
				print ptr.data,
				stack.append(ptr)
				ptr = ptr.left
			ptr = stack.pop()
			ptr = ptr.right
	def midorder(self):
		stack = []
		ptr = self
		while ptr != None or len(stack) != 0:
			while ptr != None:
				stack.append(ptr)
				ptr = ptr.left
			ptr = stack.pop()
			print ptr.data,
			ptr = ptr.right

	def mid_tree_data(self):
		stack = []
		ptr = self
		while ptr or stack:
			# if ptr:
			stack.append(ptr)
			ptr = ptr.left
			# elif stack:
			ptr = stack.pop()
			yield ptr.data
			ptr = ptr.right
	def pre_tree_data(self):
		stack = []
		ptr = self
		while ptr != None or len(stack) != 0:
			while ptr != None:
				yield ptr.data
				stack.append(ptr)
				ptr = ptr.left
			ptr = stack.pop()
			ptr = ptr.right

if __name__ == "__main__":
	root = BinaryNode(10)
	root.insert(8)
	root.insert(6)
	root.insert(13)
	root.insert1(14)
	root.insert1(1)
	root.travese(root)
	#print root.look_up(8).data
	root.preorder()
	print
	root.midorder()
	print 
	for v in root.pre_tree_data():
		print v,