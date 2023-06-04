#3
# 2562
# 최댓값
# https://www.acmicpc.net/problem/2562

num = [int(input()) for _ in range(9)]

print(max(num))
print(num.index(max(num)) + 1)