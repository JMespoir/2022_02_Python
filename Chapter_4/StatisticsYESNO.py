# 2108: Statistics  시간초과나지만 약간의 테스트케이스는 해결가능
import sys
input = sys.stdin.readline

N= int(input())
L = list(int(input()) for _ in range(N))
L.sort()


avr= round(sum(L)/N)
middle = L[N//2]
rng = L[-1]-L[0]

c = 0
max_c = 0
k = 0
for i in range(len(L)):
    if(max_c != L[i]):
        tem = L.count(L[i])
        if(c<tem):
            c = tem
            max_c = L[i]
            k=0
            continue
        if(c==tem and k==0):
            c=tem
            max_c = L[i]
            k=1

print(avr)
print(middle)
print(max_c)
print(rng)