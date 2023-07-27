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



#produtos_novo_valor = copy.deepcopy(produtos)
#for x in produtos_novo_valor:
#    x ="preco",x["preco"]*1.10
#    print(x)

