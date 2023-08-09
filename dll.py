class DLLNode:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

	def get_next(self):
		return self.next

	def get_previous(self):
		return self.prev

class DLL:
	def __init__(self):
		self.head=None

	def is_empty(self):
		return self.head is None


	def _insert_begining(self,data):
		node = DLLNode(data)
		if self.is_empty():
			self.head = node
			self.head.next,self.head.prev=None,None
			return
		else:
			temp = self.head 
			self.head=None
			self.head = node
			self.head.next = temp
			temp.prev = self.head
			temp=None

	def _insert_end(self,data):
		if self.is_empty():
			node = DLLNode(data)
			self.head = node
			self.head.next,self.head.prev=None,None
			return
		itr = self.head

		while itr.next!=None:
			itr = itr.next
		node = DLLNode(data)
		itr.next = node
		node.prev = itr

	def size(self):
		size=0
		if self.head==None:
			return 0
		itr = self.head
		while itr.next!=None:
			size+=1
			itr = itr.get_next()
		return size
	


	def _display(self):
		if self.is_empty():
			print("Linked list is empty")
			return
		itr= self.head		
		while itr!=None:
			print(itr.data)
			itr = itr.next

dll = DLL()

dll._insert_end(29)
dll._insert_begining(10)
dll._insert_end(22)
dll._insert_begining(20)
dll._insert_begining(30)
dll._insert_begining(40)
dll._insert_begining(50)

print(dll.size())
dll._display()

