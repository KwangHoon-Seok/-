from collections import deque
# 괴물 있는 부분 0, 괴물 없는 부분 1
N, M = map(int, input().split())
graph = []
goal_x, goal_y = N-1, M-1
for _ in range(N):
    graph.append(list(map(int,input())))

# 상하좌우 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(x,y):
    # if graph[x][y] == 1:
    #     graph[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        pop_x, pop_y = queue.popleft()

        for i in range(4):
            nx = pop_x + dx[i]
            ny = pop_y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[pop_x][pop_y] + 1
                queue.append((nx,ny))
                
    return graph[goal_x][goal_y]

print(bfs(0,0))