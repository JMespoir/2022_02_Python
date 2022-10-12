#2475 : Verification
def solve(n):
    return sum(map(lambda x: x**2, n))%10



N = list(map(int,input().split()))

print(solve(N))