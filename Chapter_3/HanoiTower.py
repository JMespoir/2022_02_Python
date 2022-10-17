# 1914 : HanoiTower

def solve(N,str, mid, fin):
    if(N==1):
        print(str,fin)
    else:
        solve(N-1,str,fin,mid)
        print(str, fin)
        solve(N-1,mid,str,fin)
        
        

N = int(input())
print(2**N-1)
if(N<=20):
    solve(N,'1','2','3')
    

