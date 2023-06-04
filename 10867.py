import sys
input = sys.stdin.readline
n = int(input())
res = list(map(int, input().split()))
# res.append(int(input().split()))
    # res.append(int(input()))
    
res.sort()
for i in range(n):
    if res[i] != res[i-1]:
        print(res[i] , end = ' ')
