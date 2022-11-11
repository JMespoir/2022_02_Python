#짝퉁 제곱수, 각자릿수를 모두 더하면 제곱수가 되는 수
def solve(N,M):
    cnt = 0
    for i in range(N,M+1):
        if(isS(i)):
            cnt+=1
    return cnt

def isS(n):
    k = str(n)
    res_sum = sum(map(int,k))
    if(res_sum== int(res_sum**0.5)**2):
        return True
    else:
        return False

N,M = map(int,input().split())
print(solve(N,M))