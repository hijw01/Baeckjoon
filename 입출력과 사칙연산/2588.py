A = int(input())
B = int(input())

first = B % 10
second = (B % 100 - first) / 10
third = int(B / 100)
fourth = A * first + (A * second)*10 + (A * third)*100
print(A * first)
print(int(A * second))
print(A * third)
print(int(fourth))
