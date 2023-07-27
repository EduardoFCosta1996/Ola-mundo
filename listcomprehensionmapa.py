produtos = [
    {'nome':'p1', 'preço':10,},
    {'nome':'p2', 'preço':20},
    {'nome':'p2', 'preço':30}
]

novo_preco = [
    {**produto, 'preço':produto['preço']*1.05}
    #if produto['preço']>20 else {**produto}
    for produto in produtos
]
print(*novo_preco,sep='\n')