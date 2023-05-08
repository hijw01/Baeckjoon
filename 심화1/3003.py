chess = [1, 1, 2, 2, 2, 8]
num_list = list(map(int, input().split())) #공백 기준으로 배열 입력받음

for i in range(len(chess)):
    print(chess[i] - num_list[i], end= ' ')