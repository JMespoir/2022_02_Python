# EggDrop
import random
def eggdrop(n,T):
    global cnt
    cnt +=1
    return n>=T

def solve(N,T):
    low,high = 1, N
    while low<=high:
        mid= (low+high)//2
        if(eggdrop(mid,T)):
            high = mid-1
        else: low = mid+1
    return low


N = 100
T = random.randint(1,N)
cnt = 0
print(T,solve(N,T),cnt)