lista = [
    'a',  1, 1.1, True, [0,1,2], (1,2),
    {0,1}, {'nome':'Eduardo'},
]

for item in lista:
    if isinstance (item, set):
        print(item, isinstance(item, set))
        print(item)