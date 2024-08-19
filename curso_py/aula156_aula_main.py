from sys import path


import aula156_package.modulo
from aula156_package import modulo
from aula156_package.modulo import soma

print(soma(1,2))
print(aula156_package.modulo.soma(1,5))
print(modulo.soma(3,4))
