contador = 0
while contador <= 40:
    contador += 1
    if contador == 6:
        continue
    if contador >= 10 and contador <= 20:
        print ("nao vou mostrar o numero", contador)
        continue
    
    print(contador)
    #contador += 1


print ("acabou")