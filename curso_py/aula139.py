lista = []
for x in range(3):
    for y in range(3):
        lista = (x,y)
        print(lista)

lista_2 = [
    [x for y in range(3)]
    for x in range(3)

]
print(lista_2)