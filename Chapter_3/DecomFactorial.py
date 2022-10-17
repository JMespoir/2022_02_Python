#2057 : Decomposition Factorial
def FACTORIAL(N):
    A = [1]
    for i in range(1,N):
        A.append(A[i-1]*i)

    return A

def solve(n,f,c):
    if(c<0):
        return "NO"
    elif(n- f[c]==0):
        return "YES"
    elif(n-f[c]>0):
        return solve(n-f[c],f,c-1) 
    elif(n-f[c]<0):
        return solve(n,f,c-1)


N = int(input())
factorial = FACTORIAL(20)
print(solve(N,factorial,19))
