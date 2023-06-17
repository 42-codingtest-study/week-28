#3
# 2576
# 홀수
# https://www.acmicpc.net/problem/2576

num = []
for _ in range(7):
    k = int(input())
    if k % 2 != 0:
        num.append(k)

if len(num) == 0: print(-1)
else:
    print(sum(num))
    print(min(num))