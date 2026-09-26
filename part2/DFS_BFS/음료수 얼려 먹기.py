# DFS 버전
# N, M = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input())))

# # 0: 음료 넣을 수 있는 곳 1: 가로막힌 곳
# # dsf 는 stack 구조로 사용 -> 재귀함수도 고려
# def dfs(x,y):
#     if x <= -1 or x >= N or y <= -1 or y >= M:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x+1 ,y)
#         dfs(x, y+1)
#         dfs(x, y-1)
#         return True
#     return False    
# -> 재귀 함수에 대한 이해도 필요

# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j) == True:
#             result += 1

# print(result)

# BFS 버전
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 상하좌우 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x,y):
    if graph[x][y] == 1:
        return False

    queue = deque([(x,y)])
    graph[x][y] = 1 # 방문 처리

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0: # 인접한 것들 가능한거 다 넣어
                    graph[nx][ny] = 1 # 방문 처리
                    queue.append((nx,ny))
        return True
    # -> popleft 된 원소의 주변 원소들 큐에 다 집어넣고, 하나씩 꺼내면서 작업

result = 0
for i in range(N):
    for j in range(M):
        if bfs(i, j) == True:
            result += 1

print(result)