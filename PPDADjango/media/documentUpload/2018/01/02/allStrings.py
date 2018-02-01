global myList
myList = [None] * 5
def binaryStrings(n):
	if(n < 1):
		print(myList)
	else:
		myList[n - 1] = 0
		binaryStrings(n - 1)
		myList[n - 1] = 1
		binaryStrings(n - 1)
binaryStrings(5)