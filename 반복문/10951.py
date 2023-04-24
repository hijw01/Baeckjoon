#except 활용

while 1:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break