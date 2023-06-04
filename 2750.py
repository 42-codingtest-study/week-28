n = int(input())
res = []
for i in range(n):
    res.append(int(input()))
    
res.sort()
for i in range(n):
    print (res[i])
# print(res)