#최대공약수와 최소공배술르 구하시오
def gcd(N,M):
    if(M==0):
        return N
    return gcd(M,N%M)

def lcm(N,M):
    return(N*M)//gcd(N,M)

N,M = map(int,input().split())
print(gcd(N,M))
print(lcm(N,M))