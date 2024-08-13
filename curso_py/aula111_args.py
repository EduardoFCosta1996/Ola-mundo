def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total, numero)



soma(1, 2, 3, 4, 5, 6)