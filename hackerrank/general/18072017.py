n = int(input())
a = []
for x in range(n):
    a.append(input().lower())
count = 0
sett = set()
for x in a:
    for y in x:
        sett.add(y)
    for y in sett:
        if y in "qwertyuiopasdfghjklzxcvbnm":
            count+=1
    if count == 26:
        print("YES")
        sett = set()
        count = 0
    else:
        print("NO")
        sett = set()
        count = 0