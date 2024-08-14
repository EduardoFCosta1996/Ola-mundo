def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

dois = criar_multiplicador(2)
tres = criar_multiplicador(3)
print(dois(2))
print(tres(2))
#for numero in 