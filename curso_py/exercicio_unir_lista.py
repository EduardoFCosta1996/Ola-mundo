# ['BA', 'SP', 'MG', 'RJ']
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

cidades_estados =list(zip_longest(cidades,estados,fillvalue=None))
print(cidades_estados)
