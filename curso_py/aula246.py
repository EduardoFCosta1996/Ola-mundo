from typing import Any


class Multiplicar:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self.func(*args, **kwargs)
        

@Multiplicar
def soma (x, y):
    return x*y

operacao = soma (2, 2)
print(operacao)