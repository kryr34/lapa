from .matrix import Matrix

def test_vector():
    v = Matrix(2,1).setFrom([[1],
                             [2]])
    t1 = Matrix(1,2).setFrom([[1, 2]])

    vt = v.tran()
    assert vt == t1
    print(vt)

    vt = vt.tran()
    assert vt == v
    print(vt)
