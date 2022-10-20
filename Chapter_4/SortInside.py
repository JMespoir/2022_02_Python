#1427 : Sort Inside
import sys
input = sys.stdin.readline

S = input().strip()
S = list(S)
S.sort(key=lambda x: -int(x))
print("".join(S))