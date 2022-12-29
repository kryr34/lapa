#!/bin/python

from math import pi, log
from utils import Matrix

a = Matrix(2,2).setFrom([[2, -2],
                         [3, -5]])
b = Matrix(2,2).setFrom([[-2, 0],
                         [ 4, 2]])
c = Matrix(2,3).setFrom([[-1, 2, 0],
                         [ 2, 0, 3]])
e = Matrix(3,2).setFrom([[ 2, -1],
                         [pi, log(2,10)],
                         [-2, 3]])
f = Matrix(3,3).setFrom([[1,2,3],
                         [2,3,3],
                         [3,5,7]])
i = Matrix(3,3).setFrom([[1,0,0],
                         [0,1,0],
                         [0,0,1]])

print('(a)'*20)
print(f'A+2B=\n{a+b*2}')
print(f'C-B*E^T=\n{c-b*e.tran()}')
print(f'A^T=\n{a.tran()}')

print('(b)'*20)
m = a*b
n = b*a
print(f'm=\n{m}')
print(f'n=\n{n}')
print(f"m {'==' if m==n else '!='} n")

print('(c)'*20)
p = c.tran() * b.tran()
q = (b * c).tran()
print(f'p=\n{p}')
print(f'q=\n{q}')
print(f"p {'==' if p==q else '!='} q")

print('(d)'*20)
print(f'A^-1=\n{~a}')
