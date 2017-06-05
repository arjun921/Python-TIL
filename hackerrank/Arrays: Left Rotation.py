a = input().strip().split(' ')
ls = input().strip().split(' ')
rot = int(a[1])
rott = ls[rot:]+ls[:rot]
print (*rott)
