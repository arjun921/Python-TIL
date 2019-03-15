#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""
ALgorithm
passed list = [0]
while in steps range
    if passed == step_ind:
        break
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
ind- 0 1 2 3 4 5 6

passed - 0 0 1 0 0 1 0
passed - 0

----------------------------
iter 0 === 0
skip2 = 1(2)
skip1 = 0(1)

skip1 jump
jump = 1
passed append skip1(1)
----------------------------
iter 1 === 0
skip2 = 0
skip1 = 1

skip2 jump
jump = 2
passed append 2
passed append 3
----------------------------
iter 2 === 1
step skip
----------------------------
iter 3 === 0
skip2 = 1
skip1 = 0

skip1 jump
jump = 3
passed append 4
----------------------------
iter 4 === 0
skip2 = 0
skip1 = 1

skip2 jump
jump = 4
passed append 4+1=5
passed append 4+2=6
----------------------------
iter 5 === 0
skip2 = 0
skip1 = 1

skip2 jump
jump = 4
passed append 4+1=5
passed append 4+2=6
----------------------------
iter 6 === 0
skip2 = 0
skip1 = 1

skip2 jump
jump = 4
passed append 4+1=5
passed append 4+2=6

"""