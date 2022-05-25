def shift(aList):
    n = len(aList)
    for i in range(n):
        if aList[i] != aList[n-1]:
            aList[i] = aList[i+1]
            print(aList)

        elif aList[i]==aList[i-1]:
            aList[i]=aList[0]
            print(aList)

shift(aList=[1,2,3])