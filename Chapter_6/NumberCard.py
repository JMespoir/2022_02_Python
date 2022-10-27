# 10815 : Number Card

def solve(L,NUM):
    for i in range(len(NUM)):
        k= binsearch(L,NUM[i])
        NUM[i]= k
    return NUM

def binsearch(L, num):
    high , low = len(L)-1, 0

    while(high>=low):
        mid = (high + low) //2
        if(L[mid]==num):
            return 1
        elif(L[mid]>num):
            high = mid-1
        else:
            low = mid+1
    return 0



M = int(input())
L = list(map(int,input().split()))
T = int(input())
NUM = list(map(int,input().split()))

L.sort()
NUM = solve(L,NUM)
print(" ".join(map(str, NUM)))