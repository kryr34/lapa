from .augmented_matrix import AugmentedMatrix

import numpy as np
from test import test


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
    from matrix import Matrix
    print("This is class and its test of argument matrix.")
    test_Argument.exchange()
    test_Argument.scaler()
    test_Argument.add()

