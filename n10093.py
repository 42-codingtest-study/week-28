#2
# 10093
# 숫자
# https://www.acmicpc.net/problem/10093

num = list(map(int, input().split()))
a = min(num)
b = max(num)

if b - a == 1 or a == b:
    print(0)
    exit()

num = [i for i in range(a + 1, b)]

print(len(num))
print(*num, sep=' ')