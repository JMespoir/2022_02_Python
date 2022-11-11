#스무고개 놀이 이분탐색
def binsearch(N,M,res):
    low = N
    high = M
    while(high>=low):
        mid = (low+high)//2
        if(mid == res):
            print(mid, "END")
            return
        elif(mid>res):
            high = mid-1
            print(mid, "DOWN")
        else:
            low = mid+1
            print(mid,"UP")
N,M = map(int,input().split())
ans = int(input())
binsearch(N,M,ans)