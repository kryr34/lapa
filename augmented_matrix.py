#!/bin/python

import numpy as np
from matrix import Matrix
from test import test

class AugmentedMatrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def exchange(self, ra ,rb):
        tmp = self.a.arr[ra]
        self.a.arr[ra] = self.a.arr[rb]
        self.a.arr[rb] = tmp
        tmp = self.b.arr[ra]
        self.b.arr[ra] = self.b.arr[rb]
        self.b.arr[rb] = tmp
    def rop(self, target_row, **kwargs):
        tmp = [0]*self.a.cols
        for key,value in kwargs.items():
            if key[0] == 'r':
                n = int(key[1:])
                for i in range(self.a.cols):
                    tmp[i] += self.a.arr[n][i] * value
        self.a.arr[target_row] =tmp
        tmp = [0]*self.b.cols
        for key,value in kwargs.items():
            if key[0] == 'r':
                n = int(key[1:])
                for i in range(self.b.cols):
                    tmp[i] += self.b.arr[n][i] * value
        self.b.arr[target_row] =tmp
    def toNpmatrix(self):
        return np.append(self.a.arr, self.b.arr, axis=1)

class test_Argument:
    def setup():
        a = Matrix(2,2).setFrom([[1,0],
                                 [0,1]])
        b = Matrix(2,2).setFrom([[0,1],
                                 [1,0]])
        return (a,b)
    @test
    def exchange():
        (a,b) = test_Argument.setup()
        mm = AugmentedMatrix(a,b)
        mm.exchange(0,1)
        result = mm.toNpmatrix()
        compare = np.matrix([[0,1,1,0],
                             [1,0,0,1]])
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def scaler():
        (a,b) = test_Argument.setup()
        mm = AugmentedMatrix(a,b)
        mm.rop(0, r0=2)
        result = mm.toNpmatrix()
        compare = np.matrix([[2,0,0,2],
                             [0,1,1,0]])
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def add():
        (a,b) = test_Argument.setup()
        mm = AugmentedMatrix(a,b)
        mm.rop(0, r0=1, r1=2)
        result = mm.toNpmatrix()
        compare = np.matrix([[1,2,2,1],
                             [0,1,1,0]])
        passed = np.array_equal(result, compare)
        return (result, compare, passed)

if __name__ == '__main__':
    print("This is class and its test of argument matrix.")
    test_Argument.exchange()
    test_Argument.scaler()
    test_Argument.add()

