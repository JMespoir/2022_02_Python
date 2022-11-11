#matrix A + matrix B - matrix C
def solve(A,B,C):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(int(A[i][j])+int(B[i][j])-int(C[i][j]),end =" ")
        print()

row,col = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(row)]
B = [list(map(int,input().split())) for _ in range(row)]
C = [list(map(int,input().split())) for _ in range(row)]
solve(A,B,C)