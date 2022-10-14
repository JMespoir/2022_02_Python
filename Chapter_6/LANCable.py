#1654 : LAN Cable incision lit
# def solve(l,n):
#     low,high = 1, max(l)
#     while(low<=high):
#         mid = (low+high)//2
#         cnt = count(l,mid)
#         if(cnt<n):
#             high = mid-1
#         else:
#             low = mid+1
#     return high

# def count(l,mid):
#     cnt = 0
#     for i in range(len(l)):
#         cnt += l[i]//mid
#     return cnt




# K, N =map(int,input().split())
# L = [int(input()) for _ in range(K)]
# print(solve(L,N))

# 1654 : LAN Cable incision recur
def possible(mid,A):
    cnt = 0
    for i in range(len(A)):
        cnt += i//mid
    return cnt

def binsearch(n,A,low,high):
    if low>high:
        return high
    else:
        mid = (low+high)//2
        maxn = possible(mid,A)
        if(n>maxn):
            return binsearch(n,A, low, mid-1)
        else:
            return binsearch(n,A,mid+1,high)
def solve(l,n):
    return binsearch(n,l,1,max(l))

K, N =map(int,input().split())
L = [int(input()) for _ in range(K)]
print(solve(L,N))

