def multiplicador(*args):
    total = 1
    for numeros in args:
        total *= numeros
        print(total)
        
    return total
#multiplicador(2,4,5)

numero = multiplicador(4, 2, 3)
print (numero)
