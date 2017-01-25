lis = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis.append(input('Enter Values:'))
size = []
for x in lis:
    size.append(len(x))
print(list(zip(lis,size)))
