import sys
input = sys.stdin.readline

def check(i,j,n,A):
    res = A[i][j]
    for r in range(i,i+n):
        for c in range(j,j+n):
            if(A[r][c]!= res):
                return 2
    return res

def quadtree(i,j,n,A):
    if(n==1):
        if(A[i][j]==1):
            return "B"
        else:
            return "W"
    else:
        chek = check(i,j,n,A)
        if chek <2:
            if chek == 1:
                return "B"
            else:
                return "W"
        else:
            m = n//2
            s1 = quadtree(i,j,m,A)
            s2 = quadtree(i,j+m,m,A)
            s3 = quadtree(i+m,j,m,A)
            s4 = quadtree(i+m, j+m, m,A)
            return "Q" + s1 + s2 + s3 + s4


def solve(N,L):
    return quadtree(0,0,N,L)
        


N = int(input())
L =[list(map(int,input().split())) for _ in range(N)]
print(N)
print(solve(N,L))