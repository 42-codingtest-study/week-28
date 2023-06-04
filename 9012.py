t = int(input())

for i in range(t) :
    j = input()
    f = 0

    for i in j:
        if i == "(" :
            f += 1
        elif i == ")" :
            f -= 1
        
        if f < 0 :
            break
    
    if f == 0 :
        print ("YES")

    else:
        print ("NO")