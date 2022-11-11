#에너그램수가 몇 개인지 출력하시오
def isnum(N,M):
    for i in range(len(N)):
        for j in range(len(M)):
            if(N[i]==M[j]):
                break
            elif(j == len(M)-1 and N[i]!=M[j]):
                return False
    return True

N = input()
ary = input().split()
cnt = 0
for i in range(len(ary)):
    if(isnum(N,ary[i])):
        cnt+=1
print(cnt)