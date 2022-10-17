# 16953 : Change A to B
def solve(A,B,cnt):
    if(B<A):
        return -1
    if(A==B):
        return cnt+1
    else:
        if(B%10 == 1):
            return solve(A,B//10,cnt+1)
        elif(B%2 != 1):
            return solve(A,B//2,cnt+1)
        else:
            return -1

A,B = map(int,input().split())
if(A==B):
    print(0)
else:
    print(solve(A,B,0))