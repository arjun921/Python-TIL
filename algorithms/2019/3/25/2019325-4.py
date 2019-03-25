#https://www.hackerrank.com/challenges/python-string-formatting/problem

"""
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001     
"""




def print_formatted(number):
    decimal = [str(x) for x in range(1,number+1)]
    octal = [str(oct(x)).split('o')[1] for x in range(1,number+1)]
    hexadecimal = [str(hex(x)).upper().split('X')[1] for x in range(1,number+1)]
    binary = [str(bin(x)).split('b')[1] for x in range(1,number+1)]
    padding = len(binary[-1])
    for d, o, h, b in zip(decimal,octal,hexadecimal,binary):
        d_pad = padding-len(d)
        o_pad = padding-len(o)
        h_pad = padding-len(h)
        b_pad = padding-len(b)
        s = ' '*d_pad+f'{d}'+' '+' '*o_pad+f'{o}'+' '+' '*h_pad+f'{h}'+' '+' '*b_pad+f'{b}'
        print(s)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)