#2
# 2587
# 대표값2
# https://www.acmicpc.net/problem/2587

num = [int(input()) for _ in range(5)]
num.sort()

print(sum(num) // 5)
print(num[2])