#https://www.codechef.com/MARCH19B/problems/CHNUM

T = int(input())
for x in range(T):
    N = int(input())
    A = list(map(int,input().strip().split()))
    A = [x for x in A if x>0]
    print("{} {}".format(len(A),len(A)))