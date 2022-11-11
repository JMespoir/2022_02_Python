#여러수의 최소공배수

def lcm(N,M):
    return (N*M)//gcd(N,M)

def gcd(N,M):
    if(M==0):
        return N
    return gcd(M,N%M)

N = int(input())
arr = list(map(int,input().split()))
res = lcm(arr[0],arr[1])
for i in range(2,len(arr)):
    res = lcm(res,arr[i])
print(res)