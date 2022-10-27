#6588 : Goldbach's conjecture
import sys
input = sys.stdin.readline
def solve(primes,num):
    len_primes = len(primes)
    for i in range(len_primes):
        if(primes[i] and primes[num-i]):
            a= i
            b= num-i
            print("{} = {} + {}".format(num,a,b))
            return
    print("Goldbach's conjecture is wrong.")




def makeprimes(max):
    a = [False, False] + [True]*(max-1)

    for i in range(2, max+1):
        if(a[i]):
            for j in range(i*2,max+1,i):
                a[j] = False
    return a


L =[]
max = 0
while(1):
    T = int(input())
    if(T == 0):
        break
    if(max<T):
        max = T
    L.append(T)

primes = makeprimes(max)
for i in range(len(L)):
    solve(primes,L[i])
