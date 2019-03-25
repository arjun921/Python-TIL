# https://www.hackerrank.com/challenges/designer-door-mat/problem

# dimensions = list(map(int,input().split()))
# max_y = dimensions[0]
# max_x = dimensions[1]

max_x = 21
max_y = 7
half = int((max_x-1)/2)
for y in range(int(max_y-1/2)+1):
    if y%3 == 0 or y == 1:
        c = '.|.'*y
        if len(c) > 0:
            X = 3*y
            l = ''.join(['-' for x in range(X)])
            r = ''.join(['-' for x in range(X)])
            print(l+c+r)
    # print('-'*max_y)
