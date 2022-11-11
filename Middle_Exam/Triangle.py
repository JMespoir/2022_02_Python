def solve(n):
  cnt = 0
  for x in range((n+1)//3,(n+1)//2):
    for y in range((n-x+1)//2,x+1):
      cnt+=1

n=50000
print(solve(n))