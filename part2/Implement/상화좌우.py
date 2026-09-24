N = int(input())
data = list(map(str, input().split()))
x, y = 1, 1 # 시작위치 
arrow_dict = {'U' : (-1 , 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}

for move in data:
    dx, dy = arrow_dict[move]
    if 1 <= x + dx <= N and 1 <= y + dy <= N:
        x += dx
        y += dy
    else:
        continue
print(x, y)

