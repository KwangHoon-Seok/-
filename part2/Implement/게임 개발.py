N, M = map(int, input().split())
position = list(map(int, input().split())) # position[0] = x, position[1] = y, position[2] = heading
x, y, heading = position[0], position[1], position[2]

# 방문 위치 기록 용도 0: 미방문 1: 방문
visited = [[0] * M for _ in range(N)]
visited[x][y] = 1 # 현재 위치 방문 처리

# 맵 정보 입력 0: 육지 1: 바다
_map = []
for i in range(N):
    _map.append(list(map(int, input().split())))

# 이동 방향 정의 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

turn_times = 0 # 회전 횟수
# 회전 함수
def turn_left(position):
    global turn_times
    turn_times += 1
    x, y, heading = position[0], position[1], position[2]
    rotation = [0, 0, -1] # 왼쪽으로 회전
    if heading == 0:
        heading = 3
    else:
        heading += rotation[2]
    return x, y, heading


visited_count = 1
# 시뮬레이션 시작
while True:
    # 1단계: 왼쪽으로 회전한 후, 정면이 갈 수 있는 곳인지 확인
    # 왼쪽으로 회전
    x, y, heading = turn_left([x, y, heading])
    front_x, front_y = x + dx[heading], y + dy[heading] # 정면 확인 용도
    if visited[front_x][front_y] == 0 and _map[front_x][front_y] == 0:
        x, y = front_x, front_y
        visited[x][y] = 1
        turn_times = 0
        visited_count += 1
    # 3단계
    if turn_times == 4:
        # 4번 회전해도 이동할 수 없는 경우, 뒤로 이동
        back_x, back_y = x - dx[heading], y - dy[heading]
        if 0 <= back_x < N and 0 <= back_y < M and _map[back_x][back_y] == 0 and visited[back_x][back_y] == 0:
            x, y = back_x, back_y
        else:
            break
        turn_times = 0

print(visited_count)
