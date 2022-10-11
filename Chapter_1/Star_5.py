#2442 : print Star_5
N = int(input())

for i in range(N):
    print(" "*(N-i-1)+"*"*(2*i+1))