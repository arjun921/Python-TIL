# https://www.hackerrank.com/challenges/word-order/problem

n = int(input())
storage = {}
for x in range(n):
    string = input()

    if string in storage:
        string_count = storage[string]
        storage[string] = string_count + 1
    else:
        storage[string] = 1

print(len(storage))
print(' '.join(map(str,[x for x in storage.values()])))
