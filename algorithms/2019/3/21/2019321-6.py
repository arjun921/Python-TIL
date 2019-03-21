# https://www.hackerrank.com/challenges/most-commons/problem

s = input()
storage = {}
s = [x for x in s]
s.sort()
for x in s:
    if x in storage:
        counter = storage[x]
        storage[x] = counter+1
    else:
        storage[x] = 1


sorted_count_array = list(sorted(storage.items(), key=lambda k:k[1], reverse=True))

for x in sorted_count_array[:3]:
    print(f'{x[0]} {x[1]}')