import logging

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

    def rref(self):
        '''
        reduced row echelon form
        '''
        ref = self.copy()
        zeroVector = Matrix(self.rows, 1)
        am = AugmentedMatrix(ref, zeroVector)
        c = 0
        r = 0

        logging.debug(f"before\n{ref}")
        while c < ref.cols and r < ref.rows:
            if ref.arr[r][c] == 0:
                for i in range(r, ref.rows):
                    if ref.arr[i][c] != 0:
                        logging.debug(f"exchange")
                        am.exchange(i, r)
                        break
                else:
                    c += 1
                    continue
            if ref.arr[r][c] != 1:
                logging.debug(f"normalizen")
                dic = { f'r{r}': 1/ref.arr[r][c] }
                am.rop(r, **dic)
            for i in range(ref.rows):
                if i == r:
                    continue
                if ref.arr[i][c] == 0:
                    continue
                dic = {
                        f'r{i}': 1,
                        f'r{r}': -ref.arr[i][c]
                      }
                am.rop(i, **dic)
            r += 1
        return ref

    def getNul(self):
        rref_de_mat = self.rref()
        logging.debug(f"\n{rref_de_mat}")

        free_varible_and_basis = {}
        pivots = set()
        r = 0
        for c in range(rref_de_mat.cols):
            logging.debug(f"finding pivots: r={r}, c={c}")
            pivot = rref_de_mat.arr[r][c]
            if pivot == 1:
                logging.debug(f"find pivot: r={r}, c={c}")
                pivots |= {c}
                logging.debug(f"pivots: {pivots}")
                r += 1
        logging.debug(f"pivots: {pivots}")
        for free_v in set(range(rref_de_mat.cols))-pivots:
            free_varible_and_basis[free_v] = [0] * self.cols
            free_varible_and_basis[free_v][free_v] = 1
        logging.debug(free_varible_and_basis)

        if len(free_varible_and_basis) == 0:
            logging.debug("no free varible")
            return Matrix(self.cols,1)

        for p in range(rref_de_mat.cols):
            povit = rref_de_mat.arr[p][p]
            if povit == 0:
                continue
            for i in range(p+1, rref_de_mat.cols):
                free_v = rref_de_mat.arr[p][i]
                if free_v != 0:
                    free_varible_and_basis[i][p] = -free_v
            logging.debug(free_varible_and_basis)

        number_of_base = len(free_varible_and_basis)
        basis = list(free_varible_and_basis.values())
        #basis = [Matrix(1,self.cols).setFrom([v]).tran() for v in free_varible_and_basis.values()]
        #return basis
        logging.debug(f"basis list {basis}")

        nuls = Matrix(number_of_base, self.cols).setFrom(basis)
        logging.debug(f"before transpose\n{nuls}")
        nuls = nuls.tran()
        logging.debug(f"after transpose\n{nuls}")
        return nuls
