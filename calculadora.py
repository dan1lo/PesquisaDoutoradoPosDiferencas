import numpy as np

class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def doBoot(self, dados):
        sample_mean = []
        for _ in range(1000):  #so B=10000
            sample_n = np.random.choice(dados, size=100)
            sample_mean.append(sample_n.mean())
        return sample_mean