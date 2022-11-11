#제자리수 개수
def solve(A):
    res = []
    cnt = 0
    for i in range(len(A)):
        if(A[i]==i+1):
            cnt+= 1
            res.append(A[i])
    print(cnt)
    print(" ".join(map(str,res)))
N = int(input())
ary = list(map(int,input().split()))
solve(ary)