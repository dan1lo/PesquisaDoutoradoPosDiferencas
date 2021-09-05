import numpy as np
class Bootstrap:

    def __init__(self) -> None:
        pass

    def doBoot(self, dados):
        sample_mean = []
        for _ in range(1000):  #so B=10000
            sample_n = np.random.choice(dados, size=100)
            sample_mean.append(sample_n.mean())
        return sample_mean
    def soma(self):
        return 1 + 2
   
