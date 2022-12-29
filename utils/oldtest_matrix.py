import copy
from matrix import Matrix

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
