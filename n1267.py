#3
# 1267
# 핸드폰 요금
# https://www.acmicpc.net/problem/1267

n = int(input())
call = list(map(int, input().split()))

yMoney = 0
mMoney = 0

for i in call:
    yMoney += i // 30 * 10 + 10
    mMoney += i // 60 * 15 + 15

if yMoney < mMoney: print("Y", yMoney)
elif yMoney == mMoney: print("Y", "M", yMoney)
else: print("M", mMoney)