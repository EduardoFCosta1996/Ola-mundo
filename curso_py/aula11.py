texto = "Python"
contador=0
novo = ""
for letra in texto:
    contador+=1
    novo += f'*{letra}'
    print(letra, contador)
print(novo)