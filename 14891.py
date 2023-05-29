from collections import deque

wheel = [deque(list(input().rstrip())) for _ in range(4)]
K = int(input())


def dfs(n, p, d, w2, w6):
    if n < 0 or n > 3:
        return
    if p == -1:
        i = n - 1
        if i >= 0:
            w2 = wheel[i][2]
            w6 = wheel[i][6]
            if d == -1 and wheel[n][6] != wheel[i][2]:
                wheel[i].appendleft(wheel[i].pop())
                dfs(i, n, 1, w2, w6)
            elif d == 1 and wheel[n][6] != wheel[i][2]:
                wheel[i].append(wheel[i].popleft())
                dfs(i, n, -1, w2, w6)
        i = n + 1
        if i <= 3:
            w2 = wheel[i][2]
            w6 = wheel[i][6]
            if d == -1 and wheel[n][2] != wheel[i][6]:
                wheel[i].appendleft(wheel[i].pop())
                dfs(i, n, 1, w2, w6)
            elif d == 1 and wheel[n][2] != wheel[i][6]:
                wheel[i].append(wheel[i].popleft())
                dfs(i, n, -1, w2, w6)
    else:
        if n < p:
            i = n - 1
            if i >= 0:
                if d == -1 and w6 != wheel[i][2]:
                    w2 = wheel[i][2]
                    w6 = wheel[i][6]
                    wheel[i].appendleft(wheel[i].pop())
                    dfs(i, n, 1, w2, w6)
                elif d == 1 and w6 != wheel[i][2]:
                    w2 = wheel[i][2]
                    w6 = wheel[i][6]
                    wheel[i].append(wheel[i].popleft())
                    dfs(i, n, -1, w2, w6)
        else:
            i = n + 1
            if i <= 3:
                if d == -1 and w2 != wheel[i][6]:
                    w2 = wheel[i][2]
                    w6 = wheel[i][6]
                    wheel[i].appendleft(wheel[i].pop())
                    dfs(i, n, 1, w2, w6)
                elif d == 1 and w2 != wheel[i][6]:
                    w2 = wheel[i][2]
                    w6 = wheel[i][6]
                    wheel[i].append(wheel[i].popleft())
                    dfs(i, n, -1, w2, w6)


for _ in range(K):
    n, d = map(int, input().split())
    dfs(n - 1, -1, d, wheel[n - 1][2], wheel[n - 1][6])
    if d == -1:
        wheel[n - 1].append(wheel[n - 1].popleft())
    else:
        wheel[n - 1].appendleft(wheel[n - 1].pop())

ans = 0
for i in range(4):
    if wheel[i][0] == "1":
        ans += 2**i
print(ans)
