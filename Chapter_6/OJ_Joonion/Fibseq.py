#피보나치 수 순서 찾기
def fib():
    fibs = [0,1,2,3]
    for i in range(4,1001):
        fibs.append(fibs[i-1]+2*fibs[i-2]-fibs[i-3])
    return fibs

n = input()
l =[0]*10
for i in range(len(n)):
    if(n[i]=='0'):
        l[0] +=1
    if(n[i]=='1'):
        l[1] +=1
    if(n[i]=='2'):
        l[2] +=1
    if(n[i]=='3'):
        l[3] +=1
    if(n[i]=='4'):
        l[4] +=1
    if(n[i]=='5'):
        l[5] +=1
    if(n[i]=='6'):
        l[6] +=1
    if(n[i]=='7'):
        l[7] +=1
    if(n[i]=='8'):
        l[8] +=1
    if(n[i]=='9'):
        l[9] +=1
print(l)

