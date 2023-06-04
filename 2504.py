b = input()
leng = len(b)
stack = []
tmp = 1
res = 0

for i in range(leng):
    b = b[i]   
    if b == '(':
        tmp *= 2
        stack.append(b)
    elif b == '[':
        tmp *= 3
        stack.append(b)

    elif b == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if b[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()  
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if b[i - 1] == '[':
            res += tmp
        tmp //= 3
        stack.pop() 
if stack:
    res = 0
    
print(res)