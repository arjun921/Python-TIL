def max_in_list(ls):
    largest = ls[0]
    for x in ls:
        if x>largest:
            largest = x
    return largest
def find_longest_word(a):
    return max_in_list(a)

#reads words
lis = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis.append(input('Enter Values:'))
#lengths of words
size = []
for x in lis:
    size.append(len(x))
print(list(zip(lis,size)))
print(find_longest_word(size))
