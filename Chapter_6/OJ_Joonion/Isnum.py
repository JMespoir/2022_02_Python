#제자리수찾기
def solve(A):
    low = 0
    high = len(A)-1
    while(high>=low):
        mid = (high + low)//2
        if(mid == A[mid]):
            return mid
        elif(mid> A[mid]):
            high = mid-1
        else:
            low = mid+1
    return -1
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

print(solve(A))