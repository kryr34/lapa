#!/bin/python

import copy
from augmented_matrix import AugmentedMatrix

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
        if type(other) is int or type(other) is float:
            newone = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    newone.arr[i][j] += self.arr[i][j] * other;
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

import numpy as np
from test import test

class test_Matrix:
    @test
    def constuctor():
        arr = [[1,2,3],
               [4,5,6]]
        m = Matrix(2,3).setFrom(arr)
        result = np.matrix(m.arr)
        compare = np.matrix(arr)
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def constuctor_throw():
        m = Matrix(2,3);
        arr = [[1,2],
               [4,5,6]]
        arr2 = [[4,5,6],
                [4,5,6],
                [4,5,6]]
        compare = "throw"
        result = "throw"
        try:
            m.setFrom(arr)
            result = "no throw"
        except Exception as e:
            pass
        try:
            m.setFrom(arr2)
            result = "no throw"
        except Exception as e:
            pass
        passed = result == compare
        return (result, compare, passed)
    @test
    def add():
        m1 = Matrix(1,2) .setFrom([[1,2]])
        m2 = Matrix(1,2) .setFrom([[3,4]])
        result = np.matrix((m1+m2).arr)
        compare = np.matrix([[4,6]])
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def mul():
        arr = [[1,2],
               [3,4]]
        arr2 = [[1],
                [2]]
        m1 = Matrix(2,2).setFrom(arr)
        m2 = Matrix(2,1).setFrom(arr2)
        result = np.matrix((m1*m2).arr)
        compare = np.matrix(arr) * np.matrix(arr2)
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def mulScaler():
        arr = [[1,2],
               [3,4]]
        m1 = Matrix(2,2).setFrom(arr)
        result = np.matrix((m1*2.5).arr)
        compare = np.matrix(arr) * 2.5
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def transpose():
        arr = [[1,2],
               [3,4]]
        m1 = Matrix(2,2).setFrom(arr)
        result = np.matrix((m1.tran()).arr)
        compare = np.matrix(arr).getT()
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def power():
        arr = [[1,2],
               [3,4]]
        m1 = Matrix(2,2).setFrom(arr)
        result = np.matrix((m1**14).arr)
        compare = np.matrix(arr) ** 14
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def invert():
        arr = [[0,2],
               [3,4]]
        m1 = Matrix(2,2).setFrom(arr)
        result = np.matrix((~m1).arr)
        compare = np.matrix(arr).getI()
        passed = np.array_equal(result, compare)
        return (result, compare, passed)
    @test
    def nonInvertalbe():
        arr = [[ 1,0],
               [ 0,0]]
        m1 = Matrix(2,2).setFrom(arr)
        compare = "throw"
        result = "throw"
        try:
            ~m1
        except Exception as e:
            pass
        else:
            result = "no throw"
        passed = result == compare
        return (result, compare, passed)


if __name__ == '__main__':
    print("This is class and its test of matrix.")
    test_Matrix.constuctor()
    test_Matrix.constuctor_throw()
    test_Matrix.add()
    test_Matrix.mul()
    test_Matrix.mulScaler()
    test_Matrix.transpose()
    test_Matrix.power()
    test_Matrix.invert()
    test_Matrix.nonInvertalbe()
