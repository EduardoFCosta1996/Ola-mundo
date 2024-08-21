def fabrica_de_decoradores(a,b,c):
    def fabrica_de_funcoes(func):
        print('decoradora 1')
        def aninhada (*args, **kwargs):
            print('aninahda')
            res=func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes
    

@fabrica_de_decoradores(1,2,3)
def soma(x, y):
    return x + y
multiplica = fabrica_de_decoradores(1,2,3)(lambda x , y: x*y)

total = soma(10, 5)
vezes = multiplica(10,5)
print(vezes)
print(total)