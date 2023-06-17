#2
# 2577
# 숫자의 개수
# https://www.acmicpc.net/problem/2577

mul = 1

for _ in range(3):
    mul *= int(input())

chkmul = list(map(int, str(mul)))

for i in range(10):
    print(chkmul.count(i))