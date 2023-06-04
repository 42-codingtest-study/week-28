import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range (n):
    graph.append(list(map(int, input().rstrip())))

def press(x, y, n) :
    check = graph[x][y]
    if n != 1 :
        for i in range (x, x + n):
            for j in range (y, y + n):
                if check != graph[i][j] :
                    check = -1
                    break
    if check == -1 :
        print("(", end='')
        n //= 2
        press(x, y, n)
        press(x, y + n, n)
        press(x + n, y, n)
        press(x + n, y + n, n)
        print(")", end='')
    else :
        print (check, end='')

press(0, 0, n)