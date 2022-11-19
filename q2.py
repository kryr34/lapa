#!/bin/python

from matrix import Matrix

t = Matrix(3,3).setFrom([[1/6, 1/2, 1/3],
                         [1/2, 1/4, 1/4],
                         [1/3, 1/4, 5/12]])

print(f'T^5=\n{t**5}')
print(f'T^10=\n{t**10}')
print(f'T^20=\n{t**20}')
print(f'T^30=\n{t**30}')
