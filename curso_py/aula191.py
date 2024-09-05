def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_cliente('Duh')
adiciona_cliente  ('Felipe', cliente1)

cliente1.append('edu')

cliente2 = adiciona_cliente('amora')
adiciona_cliente('nala', cliente2)
print(cliente1)
print(cliente2)
