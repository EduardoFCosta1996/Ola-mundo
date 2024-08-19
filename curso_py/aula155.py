import importlib

import aula155_m
print(aula155_m.variavel)

for i in range(10):
    importlib.reload(aula155_m)
    print(i)
print("fim")