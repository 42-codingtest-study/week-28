import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range (n):
    graph.append(list(map(int, input().split())))

while n != 1 :
    new = []
    for i in range(0, n, 2) :
        tmp = []
        for j in range (0, n, 2):
            pick = sorted([graph[i+1][j], graph[i][j+1], graph[i][j], graph[i+1][j+1]])
            tmp.append(pick[2])
        new.append(tmp)
    graph = new
    n //= 2

print(graph[0][0])

