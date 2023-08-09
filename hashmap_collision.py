class HashTable:
	def __init__(self):
		self.MAX= 10
		self.arr =[[] for i in range(self.MAX)]

	def _get_hash_(self,key):
		h = 0
		for c in key:
			h+= ord(c)
		return h%self.MAX

	def __setitem__(self,key,val):
		h = self._get_hash_(key)
		key_found = False
		for i,v in enumerate(self.arr):
			if(len(v)==2 and v[0]==key):
				self.arr[h][i]=(key,val)
				key_found=True
				break
		if not key_found:
			self.arr[h].append((key,val))

	def __getitem__(self,key):
		h = self._get_hash_(key)
		for i in (self.arr[h]):
			if i[0] == key:
				return i[1]

	def __delitem__(self,key):
		h = self._get_hash_(key)
		for i,v in enumerate(self.arr[h]):
			# In this loop we are chekcking for the tuple
			# And checking the tuple and deleting the value in the tuple 
			if v[0] == key:
				del self.arr[h][i]

h = HashTable()
h["Praveen"]= 12
h["pr"]= 12
h["SAI"]= 12

print(h["Praveen"])

del h["SAI"]
print(h.arr)