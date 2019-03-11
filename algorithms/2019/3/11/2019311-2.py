#https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    primary_diagonal = 0
    for x in range(len(arr)):
        primary_diagonal += arr[x][x]

    secondary_diagonal = 0
    
    reverse_index = len(arr)-1
    for x in arr: 
        secondary_diagonal += x[reverse_index]
        reverse_index -= 1
    
    return abs(primary_diagonal-secondary_diagonal)
    
        

if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print (result)