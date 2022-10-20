# 10448 : EurekaTheory
import sys
input = sys.stdin.readline

def solve(N,L):
    
        


    if(N==0):
        return 1
    else:
        return 0


def makeArray():
    L = list()
    i = 1
    sum = 0
    while(sum<=1000):
        L.append(sum+i)
        i+=1

    return L

L = makeArray()
N = int(input)
for i in range(N):
    print(solve(N,L))

