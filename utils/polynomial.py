import logging

import re

class Polynomial:
    '''
    one variable polynomial
    '''
    def parser(text):
        #TODO
        text = text.replace(" ", "")
        if text[0] not in ('+', '-'):
            text = "+" + text
        matches = re.findall(r"(+|-)(\d*)x(^(\d*))?", text)
    def __init__(self, *coeffs: int|float):
        self._coeffs = list(coeffs)[::-1]
        self._reduce()
    def solve(self) -> set[float]:
        '''
        get the solving where the polynomial equal zero.
        '''
        if len(self._coeffs) == 2:
            b, a = self._coeffs
            return b/a
        if len(self._coeffs) == 3:
            c, b, a = self._coeffs
            logging.debug(f"a,b,c: {a,b,c}")
            return {
                    (-b+(b**2-a*c*4)**0.5) / (a*2),
                    (-b-(b**2-a*c*4)**0.5) / (a*2)
                   }
        raise Exception("I'm too weak to solve this.")
    def __eq__(self, other):
        return other._coeffs == self._coeffs
    def __add__(self, other):
        if len(self._coeffs) < len(other._coeffs):
            self, other = other, self
        newone = Polynomial(*(self._coeffs[::-1]))
        for i, _coeffs in enumerate(other._coeffs):
            newone._coeffs[i] += _coeffs
        return newone._reduce()
    def __neg__(self):
        newone = Polynomial(*(self._coeffs[::-1]))
        for i, _coeffs in enumerate(newone._coeffs):
            newone._coeffs[i] = -_coeffs
        return newone
    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        # Polynomial * Scaler
        if type(other) is int or type(other) is float:
            return Polynomial(*([x*other for x in self._coeffs[::-1]]))

        # Polynomial * Polynomial
        newone = Polynomial(*([0]*(len(self._coeffs)+len(other._coeffs)-1)))
        for i, c in enumerate(self._coeffs):
            newone += Polynomial(*((other*c)._coeffs[::-1]+[0]*i))
        return newone._reduce()
    def _reduce(self):
        '''
        remove zero leading coeffs.
        '''
        i = len(self._coeffs)-1
        while i>0 and self._coeffs[i] == 0:
            self._coeffs = self._coeffs[:-1]
            i-=1
        return self
    def __repr__(self):
        return f"Polynomial {self._coeffs[::-1]}"


