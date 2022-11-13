class HashTable:
	def __init__(self):
		self.MAX=50
		self.arr =[0 for i in range(self.MAX)]

	def get_hash(self,key):
		h=0
		for char in key:
			h+= ord(char)
		return h%self.MAX

	def __setitem__(self,key,val):
		#getting the hash from the hash table
		h = self.get_hash(key)
		found =False
		for i in enumerate(self.arr):
			if i[0]==h:
				if i[1]>0:
					found =True
					break
		if not found:
			self.arr[h]=val
			print("Value is updated")
		print(f"In The key {h} and the value {self.arr[h]}")

	def get(self,key):
		h = self.get_hash(key)
		for i in enumerate(self.arr):
			if i[0] == h:
				if i[1]<=0 :
					print("No element found with the requested key")
					break
		return self.arr[h]
	def _get_enumerable_data(self):
		for i in enumerate(self.arr):
			print(i)
	def __delitem__(self,key):
		h = self.get_hash(key)
		self.arr[h]= None
hashTable = HashTable()

hashTable["Praveen"]=1000
hashTable["sai"] = 2000
hashTable["K"] = 100
hashTable["Praveen"]=10
# hashTable._get_enumerable_data()

del hashTable["sai"]
print(hashTable.arr)

print(hashTable.arr)