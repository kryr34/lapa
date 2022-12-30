
from .matrix import Matrix

def test_no_free_varible():
    mat = Matrix(2,2).setFrom([[1,0],
                               [0,1]])
    basis = mat.getNul()
    compare = Matrix(1,2).setFrom([[0,0]]).tran()
    print(basis)
    print(compare)
    assert basis == compare

def test_one_free_varible():
    mat = Matrix(2,2).setFrom([[1,0],
                               [0,0]])
    basis = mat.getNul()
    compare = Matrix(1,2).setFrom([[0,1]]).tran()
    print(basis)
    print(compare)
    assert basis == compare

def test_one_free_varible():
    mat = Matrix(2,2).setFrom([[1,3],
                               [0,0]])
    basis = mat.getNul()
    compare = Matrix(1,2).setFrom([[-3,1]]).tran()
    print(basis)
    print(compare)
    assert basis == compare

def test_two_free_varible():
    mat = Matrix(2,2).setFrom([[0,0],
                               [0,0]])
    basis = mat.getNul()
    compare = Matrix(2,2).setFrom([[1,0],
                                   [0,1]])
    print(basis)
    print(compare)
    assert basis == compare
