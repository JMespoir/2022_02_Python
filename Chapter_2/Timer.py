#2884 : print Timer
def solve(h,m):
    if m>=45:
        m= m-45
    else:
        m=m+15
        if(h==0):
            h=23
        else:
            h= h-1
    print(h, m)



H,M = map(int,input().split())

solve(H,M)