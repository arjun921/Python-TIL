# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# Not solved
a = input().strip()
b = input().strip()

aa = []
bb = []
deletions = 0
for x in a:
    if x not in b:
        deletions +=1
    else:
        aa.append(x)


for x in b:
    if x not in a:
        deletions +=1
    else:
        bb.append(x)
aa.sort()
bb.sort()

if len(aa)!=len(bb):
    deletions += abs(len(aa) - len(bb))
# print(aa)
# print(bb)
print(deletions)
