def solve(L,N):
    i=0
    while(i+1<N and L[i]<L[i+1]):
        i +=1
    max = i
    if(i==0 or i==N-1):
        return -1
    while(i+1<N and L[i]>L[i+1]):
        i+=1
    if(i != N-1):
        return -1
    return max
        



N = int(input())
L = []
for i in range(N):
    L.append(int(input()))

print(solve(L,N))