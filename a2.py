#!/bin/python
import logging
from colorama import Fore, Back, Style
FORMAT = Fore.RED + "[%(filename)s:%(lineno)s - %(funcName)s() ] " + Fore.BLUE + "%(message)s" + Fore.RED + "[END LOGGING]" + Fore.RESET
#logging.basicConfig(level=logging.DEBUG, format=FORMAT)

from utils import Matrix as BaseMat, Polynomial

class Matrix(BaseMat):
    def determinant(mat):
        if mat.rows != 2 or mat.cols != 2:
            raise Exception("I'm too weak to solve this.")
        return mat.arr[0][0] * mat.arr[1][1] - mat.arr[1][0] * mat.arr[0][1]

    def polynomialize(mat):
        newmat = mat.copy()
        for i in range(newmat.rows):
            for j in range(newmat.cols):
                newmat.arr[i][j] = Polynomial(mat.arr[i][j])
        return newmat
    
    def getEigenvalues(mat):
        if mat.cols != mat.rows or mat.cols != 2:
            raise Exception("I'm too weak to solve this.")
        mat = mat.polynomialize()
        #i = Matrix.Identiy(2).polynomialize()
        i = Matrix.polynomialize(BaseMat.Identiy(2))
        l =  i * Polynomial(1, 0)
        characteristic = Matrix.determinant(mat-l)
        return characteristic.solve()

    def getEigenvectorBy(mat, eigenvalue):
        mat = mat - Matrix.Identiy(2)*eigenvalue
        basis = mat.getNul()
        return basis


a = Matrix(2,2).setFrom([[-1, 2],
                         [ 0, 2]])

b = Matrix(2,2).setFrom([[1, 6],
                         [5, 2]])

c = Matrix(2,2).setFrom([[1, 2],
                         [2, 4]])

v = Matrix(2,2).setFrom([[ 7, 2],
                         [-4, 1]])

w = Matrix(2,2).setFrom([[ 3, 1],
                         [-1, 1]])

x = Matrix(2,2).setFrom([[1, 2],
                         [3, 4]])

z = Matrix(2,2).setFrom([[0, 0],
                         [0, 0]])
testcase = {
        "A": a, "B": b,
        "C": c,
        "V": v, "W": w, "X": x, "Z": z,
        }

for name, mat in testcase.items():
    print(f"test matrix {name} " + "="*40)
    logging.debug(f"\n{mat}")
    eigenvalues = mat.getEigenvalues()
    print(f"eigenvalues is {eigenvalues}")
    for eva in eigenvalues:
        eve = mat.getEigenvectorBy(eva)
        #print(f">for eigenvalue= {eva},\neigenvector=\n{eve}")
        print(f">for eigenvalue= {eva},\nbasis of eigenspace(aka eigenvectors)=\n{eve}")
