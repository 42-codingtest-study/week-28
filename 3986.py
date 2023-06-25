answer = 0
for _ in range(int(input())):
    stack = []
    s = list(input())
    for i in s:
        stack.append(i)
        while len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        answer += 1
print(answer)
