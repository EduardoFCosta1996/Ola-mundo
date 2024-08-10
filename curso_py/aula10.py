frase = "oratoroeuaroupaadoreiaaaaaaaaaaaaaade roma, rato rato roupa rei rei rei rei o o o o o"

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ""
while len(frase) > i:
    nova = frase[i]
    i+=1
    quantas_vezes_apareceu = frase.count(nova)
    if apareceu_mais_vezes < quantas_vezes_apareceu:
        apareceu_mais_vezes = quantas_vezes_apareceu
        letra_apareceu_mais_vezes = nova
print (apareceu_mais_vezes, letra_apareceu_mais_vezes)
