N, M = map(int, input().split())

ball = [i for i in range(1,N+1)]

temp = 0

for _ in range(M):
    i, j = map(int, input().split())
    temp = ball[i-1]
    ball[i-1] = ball[j-1]
    ball[j-1] = temp

    # basket[i-1], basket[j-1] = basket[j-1], basket[i-1]


for i in range(N):
    print(ball[i], end = ' ')