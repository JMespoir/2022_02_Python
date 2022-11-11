#바이토닉 수열

def solve(N,ary):
    i = 0
    while(i+1 < N and ary[i]<ary[i+1] ):
        i+= 1
    if(i+1==N or i == 0):
        return -1
    max = i
    while(i+1 < N and ary[i]>=ary[i+1]):
        i+=1
    if(i != N-1):
        return -1
    return max

N = int(input())
ary = []
for i in range(N):
    ary.append(int(input()))

print(solve(N,ary))