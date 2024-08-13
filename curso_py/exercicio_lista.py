lista = []

while True:
    print("selecione uma opçao")
    opcao = input("[i]nserir, [a]pagar, [l]ista")

    if opcao == "i":
        valor = input("digite oque quer inserir")
        lista.append(valor)
    elif opcao == "a":
        indice = input("digite o valor que quer apagar")
        
        try:
            indices = int(indice)
            del lista[indices]
        except:
            print("nao foi possivel apagar esse iten")  
    elif opcao == "l":
        if len(lista) == 0:
            print("nao á nada na lista")
        for i, valor in enumerate(lista):
            print(i,valor)   