

class BinaryTree:
	def __init__(self,data):
		self.data = data
		self.leftNode = None
		self.righNode = None

	def insertNodes(self,data):

		if data<self.data:
			if self.leftNode:
				self.leftNode.insertNodes(data)
			else:
				self.leftNode = BinaryTree(data)
				return
		else:
			if self.righNode:
				self.righNode.insertNodes(data)
			else:
				self.righNode = BinaryTree(data)
				return

	def printtree(self):
		if self.leftNode:
			self.leftNode.printtree()
		
