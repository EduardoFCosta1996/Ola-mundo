class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor
   
    @property
    def cor(self):
        return self.cor_tinta
    
'''
    def get_cor(self):
        return self.cor_tinta
'''
caneta = Caneta('azul')
print(caneta.cor) #<--- quebra o codigo pq mudou o nome para cor_tinta
#print(caneta.get_cor())