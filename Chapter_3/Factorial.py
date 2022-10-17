# 10872 : Factorial
def Factorial(N):
    if(N <=1):
        return 1
    return Factorial(N-1) * N


N = int(input())

print(Factorial(N))