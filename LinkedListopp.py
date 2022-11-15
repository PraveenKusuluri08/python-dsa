class Node:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next= next

class SingleLinkedList:
	def __init__(self):
		self.head = None

	def insertBegining(self,data):
		node = Node(data,self.head)
		self.next=self.head
		self.head=node

	def insertEnd(self,data):
		if self.head is None:
			self.insertBegining(data)
			return
		itr = self.head
		while itr.next:
			itr=itr.next

		node = Node(data,None)
		itr.next=node

	def reverseList(self):  
		current = self.head
		prev=None
		while current is not None:
			next = current.next
			current.next=prev
			prev = current
			current=next
		self.head=prev


	#this function is used to insert list at begining 
	def insertList_begining(self,data):
		self.head = None

		for i in data:
			self.insertBegining(i)

	#this function is used to insert list at end 
	def insertList_end(self,data):
		self.head =None
		for i in data:
			self.insertEnd(i)


	def countLengthOfList(self):
		count =0
		itr = self.head
		while itr:
			count+=1
			itr = itr.next

		return count

	def insertPosition(self,data,index):
		itr = self.head
		node = Node(data,None)
		if index<1:
			print("Index must be greater than one\n")
			return
		if  index==1:
			self.insertBegining(data)
			return
		elif index==self.countLengthOfList():
			self.insertEnd(data)
			return
		elif index> self.countLengthOfList():
			print("List is underflow\n")
			return
		else:
			for i in range(1,index-1):
				if itr!=None:
					itr= itr.next
				if itr!=None:
					node.next = itr.next
					itr.next = node
					return
			return

	def deleteBegining(self):
		itr = self.head
		if self.head is None:
			print("No elements in the given list")
			return
		else:
			self.head = itr.next

	def deleteEnd(self):
		itr = self.head
		if itr is None:
			print("No elements in the given list")
			return
		else:
			if itr.next==None:
				self.head=None
			else:
				while(itr.next.next!=None):
					itr = itr.next


				last = itr.next
				itr.next= None
				last = None

	def delete_at_index(self,index):
		if self.head ==None:
			print("Linked list is empty")
			return

		if index==0:
			return self.deleteBegining()

		if index>= self.countLengthOfList():
			return self.deleteEnd()

		count =0
		itr = self.head

		while itr:
			if count == index-1:
				itr.next = itr.next.next
				break
			itr = itr.next
			count+=1

    # this function is based on insertion of value after the value which is querying
    # this function insert value which is first foud at query

	def insertValueAfterValue(self,dataQeury,data):
		if self.head is None:
			return

		if self.head.data == dataQeury:
			self.head.next = Node(data,self.head.next)
			return

		itr = self.head
		while itr:
			if itr.data == dataQeury:
				itr.next = Node(data,itr.next)
				return
			itr = itr.next

	def removeValueAfterValue(self,dataQeury):
		if self.head is None:
			return
		if self.head.data == dataQeury:
			self.head = self.head.next
			return
		itr = self.head
		while itr:

			if itr.next.data == dataQeury:
				itr.next.next = itr.next.next.next
				break
			if itr.next.next.next ==None :
				print("No elements left after this element")
				return
			itr = itr.next

	def removeByValue(self,dataQeury):
		if self.head is None:
			return
		if self.head.data == dataQeury:
			self.head = self.head.next
		itr = self.head
		while itr:
			if itr.next.data == dataQeury:
				itr.next = itr.next.next
				break
			if itr.next.next ==None:
				print("No elements left after this element")
			itr = itr.next

	def returnHeadNode(self):
		return self.head

	def linkedListToArray(self):
		len = self.countLengthOfList()
		itr = self.head
		lt = []
		while itr:
			lt.append(itr.data)
			itr = itr.next
		return lt

	def reverseConvertedList(self):
		lt = self.linkedListToArray()

		return lt[::-1]

	def singleLinkedListToCircular(self):
		itr = self.head

		while self.head.next is not None:
			self.head = self.head.next
		
		self.head.next = itr
		print("Linked list is circular",itr.data)

	def arrayToLinkedList(self,arr):
		n = len(arr)

		root = None
		

	def printList(self):
		if self.head is None:
			print("Linked list is empty")
			return
		itr = self.head
		listData =""
		while itr:
			listData +=str(itr.data)+"-->"
			itr = itr.next
		print(listData)

	# Sort the linked list using selection sort
	def swap(self,arr,i,j):
		temp = arr[i]
		arr[i]=arr[j]
		arr[j]= temp
	def sortLinkedList(self):
		listData =[]
		if self.head is None:
			print("Linked list is empty cannot able sort")
			return
		itr = self.head
		while itr:
			listData.append(itr.data)
			itr = itr.next
		#Selection sort from here
		n = len(listData)
		for i in range(n):
			min=i
			for j in range(i+1,n):
				if listData[j]<listData[min]:
					min =j
			self.swap(listData,i,min)
		print("Sorted  list data")
		print(listData)


ll = SingleLinkedList()
ll.insertBegining(12)
ll.insertBegining(13)
ll.insertBegining(14)
ll.insertEnd(1)
ll.insertEnd(2)
# ll.insertList_end([1,2,3,4,5,6,7,8,9])
# ll.deleteBegining()
print("The length of the list is ",ll.countLengthOfList())
# ll.insertPosition(99,1)
# ll.insertValueAfterValue(1,11)
# ll.removeByValue(11)
# ll.deleteEnd()
ll.printList()
print(ll.linkedListToArray())
print("reverseList is ",ll.reverseConvertedList())
# ll.singleLinkedListToCircular()
# ll.reverseList()
# ll.delete_at_index(4)

ll.sortLinkedList()
