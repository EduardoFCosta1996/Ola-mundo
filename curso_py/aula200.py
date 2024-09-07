class carro:
    def __init__(self,nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} Está acelerando')
        

fusca = carro('Fusca')
print(fusca.nome)

celta = carro('Celta')
print(celta.nome)
print(celta.acelerar())

