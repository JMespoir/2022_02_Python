def solve(n):
    for m in range(1,n+1):
        if(n == m+sum(map(int,str(m)))):
            return m
    return 0
N = int(input())
print(solve(N))