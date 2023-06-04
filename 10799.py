import sys

def count_iron(ir):
    stack = list()
    cnt = 0
    i = 0
    while (i < len(ir)):
        if (ir[i] == '('):
            if (ir[i+1] == ')'):
                cnt += len(stack)
                i += 2
            else:
                stack.append(ir[i])
                i += 1
        elif (ir[i] == ')'):
            cnt += 1
            stack.pop()
            i += 1
    return cnt


if __name__ == '__main__':
    ir = sys.stdin.readline()
    ir = ir[:len(ir) - 1]
    res = count_iron(ir)
    print(res)