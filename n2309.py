#1
# 2309
# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

import itertools

dwarf = [int(input())for _ in range(9)]

for i in itertools.combinations(dwarf, 7):
    if sum(i) == 100:
        dwarf7 = [j for j in sorted(i)]
        print(*dwarf7, sep='\n')
        exit()