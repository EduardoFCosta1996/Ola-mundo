def soma(*args):
    total = 0
    for numeros in args:
        total+=numeros
        
    return total

soma1 = soma(1, 2, 3, 4)
print(soma1)
soma2 = soma(2,3,4)
print (soma2)
