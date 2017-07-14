"""Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n."""

def filter_long_words(lis,i):
    temp = []
    for x in lis:
        if len(x)>n:
            temp.append(x)
    return temp

#reads words
lis = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis.append(input('Enter Values:'))
#lengths of words
size = []
for x in lis:
    size.append(len(x))

i = input('Enter Number')
y =filter_long_words(lis,i)
for x in y:
    print (x)
