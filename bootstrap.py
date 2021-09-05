import numpy as np
class Bootstrap:

    def __init__(self):
        pass
    def soma(self):
        return 1 + 2

    def doBoot(self, dados, tamanho):
        sample_mean = []
        for _ in range(1000):  #so B=10000
            sample_n = np.random.choice(dados, size=tamanho)
            sample_mean.append(sample_n.mean())
        return sample_mean

   
