from .polynomial import Polynomial

def notest_parser():
    assert False
    Polynomial.parser('2x^2+x-4')

def test_add():
    p1 = Polynomial(3, 2, 1)
    p2 = Polynomial(2, -1, 1)
    result = p1+p2
    assert result == Polynomial(5, 1, 2)

def test_add_wtih_zerocoeffs():
    p1 = Polynomial(2, 3, 1, 1)
    p2 = Polynomial(-2, -2, -1, 1)
    result = p1+p2
    assert result == Polynomial(1, 0, 2)

def test_mul_scaler():
    p1 = Polynomial(1, -3)
    result = p1*2
    assert result == Polynomial(2, -6)
def test_mul__polynomial():
    p1 = Polynomial(1, -3)
    p2 = Polynomial(2, -1)
    result = p1*p2
    assert result == Polynomial(2, -7, 3)

def test_solve():
    p1 = Polynomial(1, -3)
    p2 = Polynomial(1, -2)
    result = (p1*p2).solve()
    assert result == {2,3}
def test_solve2():
    p1 = Polynomial(1, -3)
    result = (p1*p1).solve()
    assert result == {3}
