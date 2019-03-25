# https://www.hackerrank.com/challenges/designer-door-mat/problem

dimensions = list(map(int,input().split()))
max_y = dimensions[0]
max_x = dimensions[1]

"""Size: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|. .|. .|. .|. .|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
"""

# max_x = 33
# max_y = 11

def pattern_triangle(y,max_x):
        c = '.|.'*y
        X = max_x - len(c)
        X = int(X/2)
        l = ''.join(['-' for x in range(X)])
        r = ''.join(['-' for x in range(X)])
        return (l+c+r)

for y in range(int(max_y-1/2)):
        if y%2 !=0:                
                line = pattern_triangle(y,max_x)
                print(line)

mid = (max_x-len('WELCOME'))/2
mid = int(mid)
print('-'*mid +'WELCOME'+ '-'*mid )

for y in range(int(max_y-1/2),0,-1):
        if y%2 !=0:                
                line = pattern_triangle(y,max_x)
                print(line)
