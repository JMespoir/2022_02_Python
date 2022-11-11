#머지가 뭐지 ? 문자열 S,T를 입력으로 받아 두 문자열의 문자들을 알파벳 순서로 출력 S는 대문자 T는 소문자

A,B = input().split()
A=list(A.upper())
B = list(B.lower())
C= A + B
C.sort(key=lambda x: (ord(x.upper()),-ord(x)))
for i in range(len(C)):
    print(C[i],end=" ")