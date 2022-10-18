# 2447 : printStar_10
from sys import stdin
def Star(N,A,start_row, start_col,fin_row,fin_col):
    if(N==3):
        for i in range(start_row,fin_row):
            for j in range(start_col,fin_col):
                A[i][j]='*'
        A[start_row+1][start_col+1] = ' '
    else:
        A= Star(N//3,A,start_row,start_col,fin_row-(N//3*2),fin_col-(N//3*2))
        A= Star(N//3,A,start_row,start_col+(N//3),fin_row-(N//3*2),fin_col-(N//3))
        A= Star(N//3,A,start_row,start_col+(N//3*2),fin_row-(N//3*2),fin_col)
        A= Star(N//3,A,start_row+(N//3),start_col,fin_row-(N//3),fin_col-(N//3*2))

        A= Star(N//3,A,start_row+(N//3),start_col+(N//3*2),fin_row-(N//3),fin_col)
        A= Star(N//3,A,start_row+(N//3*2),start_col,fin_row,fin_col-(N//3*2))
        A= Star(N//3,A,start_row+(N//3*2),start_col+(N//3),fin_row,fin_col-(N//3))
        A= Star(N//3,A,start_row+(N//3*2),start_col+(N//3*2),fin_row,fin_col)       
    return A


def solve(N):
    A= [[" "]*N for i in range(N)]
    Star(N,A,0,0,N,N)
    for i in range(N):
        for j in range(N):
            print(A[i][j],end="")
        print()

N = int(stdin.readline())
solve(N)