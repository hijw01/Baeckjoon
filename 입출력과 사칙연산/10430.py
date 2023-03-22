sA, sB, sC = input().split()

A = int(sA)
B = int(sB)
C = int(sC)

print((A+B) % C)
print(((A % C) + (B % C)) % C)
print((A*B) % C)
print(((A % C) * (B % C)) % C)
