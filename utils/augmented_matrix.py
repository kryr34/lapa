import logging

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
        logging.debug(f"rop target:{target_row} <- {kwargs}")
        tmp = [0]*self.a.cols
        for key,value in kwargs.items():
            if key[0] == 'r':
                n = int(key[1:])
                for i in range(self.a.cols):
                    logging.debug(f"Today is friday {tmp[i]}")
                    what = self.a.arr[n][i] * value
                    what = round(what*1000000)/1000000
                    logging.debug(f"in CA {self.a.arr[n][i]} * {value} |> round= {what}")
                    tmp[i] += what
                    logging.debug(f"shoot! {tmp[i]}")
        self.a.arr[target_row] =tmp
        tmp = [0]*self.b.cols
        for key,value in kwargs.items():
            if key[0] == 'r':
                n = int(key[1:])
                for i in range(self.b.cols):
                    tmp[i] += self.b.arr[n][i] * value
        self.b.arr[target_row] =tmp
        logging.debug(f"\n{self.a}")
    def toNpmatrix(self):
        return np.append(self.a.arr, self.b.arr, axis=1)

