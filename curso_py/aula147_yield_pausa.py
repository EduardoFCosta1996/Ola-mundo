def generator(n=0):
    yield 1 #pausa
    print('continuando')
    yield 2
    print('mais uma...')
    yield 3
    print('vou terminar')
    return 'acabou'
gen = generator(n=0)
for n in gen:
    print(n)
