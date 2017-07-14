Pmb = float(input())
Pmt = 1 - Pmb
Pab = float(input())
Pat = 1 - Pab
P1 = float(input())

prs = P1*(Pmb*Pat)+P1*(Pab*Pmt)
print("%2f"%prs)
