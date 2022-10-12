# 1110 : Plus Cycle
def solve(n):
    m,cnt = n,1
    while(True):
        s= sum(map(int,list(str(m))))
        m = (m%10)*10+(s%10)
        if(m==n):
            break
        cnt = cnt +1
    return cnt



N = int(input())
print(solve(N))