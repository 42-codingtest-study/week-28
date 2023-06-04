# 몇단지니 꿀단지?
import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().rstrip())))

def dfs(x, y):
	global cnt
	if x < 0 or x >= n or y < 0 or y >= n :
		return False
	if graph[x][y] == 1 :
		graph[x][y] = 0
		cnt += 1
		dfs(x + 1, y)
		dfs(x - 1, y)
		dfs(x, y + 1)
		dfs(x, y - 1)
		return True
	return False

home = 0
cnt = 0
town = []
for i in range(n) :
	for j in range(n):
		if dfs(i, j) :
			home += 1
			town.append(cnt)
			cnt = 0

print(home)
town.sort()
print('\n'.join(map(str, town)))
