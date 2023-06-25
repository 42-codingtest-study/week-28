import sys

input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in lst:
    print(i)
