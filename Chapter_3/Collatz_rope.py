#5393 : Collatz Rope
from sys import stdin   

T = int(stdin.readline())
for i in range(T):
    N = int(stdin.readline())
    print((N+1)//2*2  -((N-1)//3+1)//2 )


