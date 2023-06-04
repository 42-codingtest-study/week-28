# 재준이니?
import sys
sys.setrecursionlimit(10**6)
n = int(input())

graph = []
for _ in range (n):
    graph.append(list(map(str, input())))

def dfs(x, y, color) :
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    if graph[x][y] == color :
        if color == 'B' :
            graph[x][y] = 'b'
        elif color == 'b' or color == 'x' :
            graph[x][y] = 0
        else :
            graph[x][y] = 'x'
        dfs(x + 1, y, color)
        dfs(x - 1, y, color)
        dfs(x, y + 1, color)
        dfs(x, y - 1, color)
        return True
    return False 

r_cnt = 0
g_cnt = 0
b_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'B' :
            if dfs(i, j, 'B'):
                b_cnt += 1
        elif graph[i][j] == 'R':
            if dfs(i,j, 'R'):
                r_cnt += 1
        else :
            if dfs(i,j, 'G'):
                g_cnt += 1
print(b_cnt + r_cnt + g_cnt, end=' ')

rg_cnt = 0
b_cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'b' :
            if dfs(i, j, 'b'):
                b_cnt += 1
        elif graph[i][j] == 'x':
            if dfs(i,j, 'x'):
                rg_cnt += 1
print(b_cnt + rg_cnt)