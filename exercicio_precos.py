import copy

produtos = [
    {"Nome": "Arroz", "preco": 13.00},
    {"Nome": "Feijâo", "preco": 9.00},
    {"Nome": "Farinha", "preco": 6.00},
    {"Nome": "Bolacha", "preco": 3.00},
    {"Nome": "Café", "preco": 8.00},
]
#for x in produtos:
#    print("preco", x["preco"])
#"preco",x["preco"]*1.10
novo_preco = copy.deepcopy(produtos)
novo_preco = [
    {**produto, "preco":produto["preco"]*1.10}
    for produto in produtos
        
]
print(*novo_preco, sep="\n")

print("-------------------------------------------------")

def ordena_preco(item):
    return item["preco"]

lista_preco = produtos
lista_preco.sort(key=ordena_preco )
for nova_ordem in lista_preco:
    print(nova_ordem)


print("-------------------------------------------------")


def ordem_nome(item_nome):
    return item_nome["Nome"]

lista_nome = produtos
lista_nome.sort(key=ordem_nome)
for lista_por_nome in lista_nome:
    print(lista_por_nome)
    

#produtos_novo_valor = copy.deepcopy(produtos)
#for x in produtos_novo_valor:
#    x ="preco",x["preco"]*1.10
#    print(x)

