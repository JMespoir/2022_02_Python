#N보다크거나같고푀보다작거나같은수들의합S
def solve(s,f):
    S = 0
    for i in range(s,f+1):
        S += i
    return S


S = int(input())
F = int(input())
print(solve(S,F))