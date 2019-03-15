#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""
ALgorithm
passed list = [0]
while in steps range
    if step is end
        exit
    if step is 1 or if step has passed.
        pass
    else
        skip2 = step_i + 2
        skip1 = step_i + 1
        if skip2 exists and is safe
            passed append skip1_index
            passed append skip2_index
            jump
            pass
        else if skip 1 is safe
            passed append skip1
            jump
            pass
    
return jump

in - 0 0 1 0 0 1 0
ind- 1 2 3 4 5 6 7

passed - 1 2 

iter 1 === 0
skip2 = 1
skip1 = 0

skip1 jump
jump = 1
----------------------------
iter 2 === 0
skip2 = 0
skip1 = 1

skip2 jump
jump = 2
----------------------------
iter 3 === 1
step skip
----------------------------
iter 4 === 0
skip2 = 1
skip1 = 0

skip1 jump
jump = 3
----------------------------
iter 5 === 0
skip2 = 0
skip1 = 

skip2 jump
jump = 2


"""