class Caneta:
    def __init__(self,cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
        def cor(self, dois):
            self._cor = dois
caneta = Caneta('Azul')
caneta.cor = 'rosa'
caneta.cor = 'roxca'
print(caneta.cor)
    
        