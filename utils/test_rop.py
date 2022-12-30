from .matrix import Matrix
from .augmented_matrix import AugmentedMatrix

def test_WHY():
    mat = Matrix(2,2).setFrom([[5., 6.],
                               [5., 6.]])
    zerovec = Matrix(2,1)
    am = AugmentedMatrix(mat, zerovec)

    am.rop(0, r0=0.2)
    am.rop(1, r1=1, r0=-5.)

    com = Matrix(2,2).setFrom([[1., 1.2],
                               [0., 0.]])
    print(mat)
    print(com)
    assert mat == com

