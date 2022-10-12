#swap only use XOR

from operator import xor


A,B = map(int,input().split())

A = xor(A,B)
B = xor(B,A)
A = xor (A,B)
print (A,B)
