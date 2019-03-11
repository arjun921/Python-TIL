import random
T = int(input())

for x in range(T):
    bounds = list(map(int,input().split()))
    N = int(input())
    guess_list = [x for x in range(bounds[0]+1,bounds[1]+1)]
    while N!=0:
        guess = random.choice(guess_list)
        print(guess)
        feedback = input()
        if feedback == 'CORRECT':
            break
        elif feedback == 'TOO_SMALL':
            guess_index = guess_list.index(guess)
            guess_list = guess_list[guess_index:]
        elif feedback == 'TOO_BIG':
            guess_index = guess_list.index(guess)
            guess_list = guess_list[:guess_index]
        N -= 1
