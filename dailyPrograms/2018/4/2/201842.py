a = int(input())

answers = []
for x in range(a):
    n = int(input())
    ans = 0
    for y in range(1,n):
        ans += 1
    answers.append(str(ans))

print('\n'.join(answers))
