#양의 정수 N의 모든 약수의 합을 구하시오
def solve(N):
    res = 0
    for i in range(1,N+1):
        if(N%i == 0):
            res+= i
    return res


N = int(input())
print(solve(N))