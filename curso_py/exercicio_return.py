def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    if total % 2 == 0:
        return f'{total},é par'
    return f'{total}, é impar'
    

soma = multi(3,3)
print(soma)