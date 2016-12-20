def getList():
	listLen = int(input("Enter list length"))
	MyList=[]
	for i in range(0,listLen):
		MyList.append ( int (input("Enter Numbers in list")))
	return MyList

def firstLast(MyList):
	newList = []
	newList.append(MyList[0])
	print(len(MyList))
	newList.append(MyList[(len(MyList)-1)])
	return newList


MyList=getList()

print(firstLast(MyList))
