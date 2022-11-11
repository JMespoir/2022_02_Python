#N까지 약수의 합을 구하시오
def solve(N):
    sum = 0
    for i in range(1,int(N**0.5)+1):
        if(N%i == 0):
            sum += i
            sum += N//i
        if(i**2 == N):
            sum -= i
    return sum

N = int(input())
print(solve(N))