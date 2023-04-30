num = []
for _ in range(9):
    i = int(input())
    num.append(i)
# numbers = [int(input()) for _ in range(9)]

print(max(num))
print(num.index(max(num))+1)