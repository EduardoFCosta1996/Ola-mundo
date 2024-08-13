def soma(*args):
    total = 0
    for numeros in args:
        total += numeros
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)
soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

numeros = 10, 55,33,84
nova_soma = soma(*numeros)
print(nova_soma)
print(sum(numeros))

