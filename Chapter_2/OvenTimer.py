#2525 : Oven Timer
def solve(h,m,a):
    res = (m+ h*60 +a)%1440
    print(res//60, res%60)



H,M = map(int,input().split())
A = int(input())

solve(H,M,A)