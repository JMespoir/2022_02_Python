#swap only use plus and minus

A,B = map(int,input().split())

A = A+B
B = A-B
A = A-B
print(A,B)