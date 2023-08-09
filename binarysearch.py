n = int(input("Enter the size of the list: "))

lt = []

for i in range(0, n):
    lt.append(int(input("Enter the element: ")))

lt.sort()

searchElement = int(input("Enter the element to be searched: "))

low = 0
high = len(lt)-1


def bs(arr, low, high, searchElement):
    while low <= high:
        mid = low+(high-low)//2
        if arr[mid] == searchElement:
            return mid
        elif arr[mid] < searchElement:
            bs(arr,low,mid-1,searchElement)
        else:
            bs(arr,mid+1,high,searchElement)
    return -1


result = bs(lt, low, high, searchElement)

print(result)
