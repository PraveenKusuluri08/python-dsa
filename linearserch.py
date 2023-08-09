
# Enter the size of the array

n = int(input("Enter the size of the list: "))

lt= []

for i in range(0,n):
    lt.append(int(input("Enter the element: ")))

# Enter the element to be searched

searchElement = int(input("Enter the element to be searched: "))

ele ={}

for i in range(0,n):
    ele[i]= lt[i]

print(ele)


for i in range(0,n):
    if searchElement==lt[i]:
        print("Element found at position: ",i+1)
        break

