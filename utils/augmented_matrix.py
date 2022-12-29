class AugmentedMatrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def exchange(self, ra ,rb):
        tmp = self.a.arr[ra]
        self.a.arr[ra] = self.a.arr[rb]
        self.a.arr[rb] = tmp
        tmp = self.b.arr[ra]
        self.b.arr[ra] = self.b.arr[rb]
        self.b.arr[rb] = tmp
    def rop(self, target_row, **kwargs):
        '''
        Row OPerate
        '''
        tmp = [0]*self.a.cols
        for key,value in kwargs.items():
            if key[0] == 'r':
                n = int(key[1:])
                for i in range(self.a.cols):
                    tmp[i] += self.a.arr[n][i] * value
        self.a.arr[target_row] =tmp
        tmp = [0]*self.b.cols
        for key,value in kwargs.items():
            if key[0] == 'r':
                n = int(key[1:])
                for i in range(self.b.cols):
                    tmp[i] += self.b.arr[n][i] * value
        self.b.arr[target_row] =tmp
    def toNpmatrix(self):
        return np.append(self.a.arr, self.b.arr, axis=1)

