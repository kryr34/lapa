from .matrix import Matrix

def test_rref():
    mat = Matrix(2,2).setFrom([[1,2],
                               [1,2]])

    mat2 = Matrix(2,2).setFrom([[1,2],
                                [0,0]])
    assert mat.rref() == mat2

def ntest_rref2():
    mat = Matrix(3,3).setFrom([[1,2,3],
                               [1,3,4],
                               [1,2,4]])

    mat2 = Matrix(3,3).setFrom([[1,0,0],
                                [0,1,0],
                                [0,0,1]])
    assert mat.rref() == mat2

def test_rref3():
    mat = Matrix(3,3).setFrom([[1,2,3],
                               [1,3,4],
                               [1,2,3]])

    mat2 = Matrix(3,3).setFrom([[1,0,1],
                                [0,1,1],
                                [0,0,0]])
    assert mat.rref() == mat2

def test_rref4():
    mat = Matrix(3,3).setFrom([[1,0,2],
                               [0,1,4],
                               [0,0,0]])

    mat2 = Matrix(3,3).setFrom([[1,0,2],
                                [0,1,4],
                                [0,0,0]])
    assert mat.rref() == mat2

def test_rref4():
    mat = Matrix(3,3).setFrom([[0,1,2],
                               [0,3,6],
                               [0,2,4]])

    mat2 = Matrix(3,3).setFrom([[0,1,2],
                                [0,0,0],
                                [0,0,0]])
    assert mat.rref() == mat2
