# 퀸자식
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dx = [1, 1, -1, -1, -2, -2, 2, 2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def dfs(x, y, goal_x, goal_y) :
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x == goal_x and y == goal_y :
            break
        for i in range (8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l :
                continue
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


for _ in range(T):
    l = int(input())
    graph = [[0 for _ in range (l)] for _ in range (l)]
    start_x, start_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    dfs(start_x, start_y, goal_x, goal_y)
    print(graph[goal_x][goal_y])