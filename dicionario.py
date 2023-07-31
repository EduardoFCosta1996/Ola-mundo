
pessoa = {
    'nome': 'Eduardo',
    'sobrenome': 'Costa',
    'idade': 27,
    'altura': 1.70,
    'endereços': [
        {'rua': 'Visconde de Inhauma', 'número': 40},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])