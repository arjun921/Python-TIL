test_in = [
    [1, 3, 2, 1],
    [1, 3, 2],
    [1, 2, 1, 2],
    [3, 6, 5, 8, 10, 20, 15],
    [1, 1, 2, 3, 4, 4],
    [1, 4, 10, 4, 2],
    [10, 1, 2, 3, 4, 5],
    [1, 1, 1, 2, 3],
    [0, -2, 5, 6],
    [1, 2, 3, 4, 5, 3, 5, 6],
    [40, 50, 60, 10, 20, 30],
    [1, 1],
    [1, 2, 5, 3, 5],
    [1, 2, 5, 5, 5],
    [10, 1, 2, 3, 4, 5, 6, 1],
    [1, 2, 3, 4, 3, 6],
    [1, 2, 3, 4, 99, 5, 6],
    [123, -17, -5, 1, 2, 3, 12, 43, 45],
    [3, 5, 67, 98, 3]
]

test_out = [
    False,
    True,
    False,
    False,
    False,
    False,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    False,
    False,
    True,
    True,
    True,
    True,

]

# a = list(map(int,input().split(',')))
# a_bak = a.copy()


def sol_1(a):
    # sol 1
    b = [min(a)]
    for x in a:
        if b[-1]<x:
            b.append(x)
    diff = abs(len(b)-len(a))
    print(diff)
    print(b)
    if diff==1:
        return (True)
    else:
        return (False)
    # sol 1 ends

def check_unique_diff(a):
    a_ = set(a)
    unique_diff = len(a)-len(a_)
    print(unique_diff)
    return unique_diff>=1



def run(a):
    if check_unique_diff(a):
        return (False)
    else:
        if sol_1(a):
            return (True)
        else:
            a.remove(max(a))
            if sol_1(a):
                return (True)
            else:
                a_bak.remove(min(a_bak))
                return (sol_1(a_bak))
    
for x in zip(test_in,test_out):
    test_case = x[0]
    expected = x[1]
    out = run(test_case)
    if out == expected:
        pass
    else:
        print(x)
        break