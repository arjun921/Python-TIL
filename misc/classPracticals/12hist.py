def histogram(lis):
    for x in lis:
        print ('*'*int(x))

lis = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis.append(input('Enter Values:'))
histogram(lis)
