# https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())
storage = {}
for x in range(n):
    name = input()
    mark = str(float(input()))
    if mark in storage:
        names = storage[mark]
        names.append(name)
        storage[mark] = names
    else:
        names = []
        names.append(name)
        storage[mark] = names

marks_list = list(map(float,storage.keys()))
marks_list.sort()
second_lowest = marks_list[1]
names = storage[str(second_lowest)]
names.sort()
for name in names:
    print(name)
