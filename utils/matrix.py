#!/bin/python

import numpy as np
import copy
from .augmented_matrix import AugmentedMatrix

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.arr = [[0 for _ in range(cols)] for _ in range(rows)]
    def setFrom(self, arr):
        if len(arr) != self.rows:
            raise Exception("number of rows doesn't match")
        for row in arr:
            if len(row) != self.cols:
                raise Exception("number of cols doesn't match")
        self.arr = copy.deepcopy(arr)
        return self
    def copy(self):
        return copy.deepcopy(self)
    def __add__(self, other):
        if self.rows != other.rows:
            raise Exception("number of rows doesn't match")
        if self.cols != other.cols:
            raise Exception("number of cols doesn't match")
        newone = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                newone.arr[i][j] = self.arr[i][j] + other.arr[i][j]
        return newone
    def __sub__(self, other):
        if self.rows != other.rows:
            raise Exception("number of rows doesn't match")
        if self.cols != other.cols:
            raise Exception("number of cols doesn't match")
        newone = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                newone.arr[i][j] = self.arr[i][j] - other.arr[i][j]
        return newone
    def __mul__(self, other):
        if type(other) is not Matrix:
            newone = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    newone.arr[i][j] = self.arr[i][j] * other;
            return newone

        if self.cols != other.rows:
            raise Exception("number of rows and cols doesn't match")
        newone = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    newone.arr[i][j] += self.arr[i][k] * other.arr[k][j]
        return newone
    def tran(self):
        newone = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                newone.arr[j][i] = self.arr[i][j]
        return newone
    def __pow__(self, n):
        newone = Matrix(self.rows, self.cols).setFrom(self.arr)
        for _ in range(n-1):
            newone *= self
        return newone
    def Identiy(n):
        newone = Matrix(n,n);
        for i in range(n):
            newone.arr[i][i] = 1
        return newone
    def __invert__(self):
        if self.cols != self.rows:
            raise Exception("I'm too weak to solve this.")
        oldone = Matrix(self.rows, self.cols).setFrom(self.arr);
        invert = Matrix.Identiy(self.cols)
        am = AugmentedMatrix(oldone, invert)
        for p in range(self.cols):
            if oldone.arr[p][p] == 0:
                for i in range(p, oldone.rows):
                    if oldone.arr[i][p] != 0:
                        am.exchange(i, p)
                        break
                else:
                    raise Exception("matrix is non-invertable")
            if oldone.arr[p][p] != 1:
                dic = { f'r{p}': 1/oldone.arr[p][p] }
                am.rop(p, **dic)
            for i in range(oldone.rows):
                if i == p:
                    continue
                if oldone.arr[i][p] == 0:
                    continue
                dic = {
                        f'r{i}': 1,
                        f'r{p}': -oldone.arr[i][p]
                      }
                am.rop(i, **dic)
        return invert
    def __eq__(self, other):
        if self.rows != other.rows:
            return False
        if self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.arr[i][j] != other.arr[i][j]:
                    return False
        return True
    def __str__(self):
        return str(np.matrix(self.arr))

