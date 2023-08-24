caminho_arquivo = "aulaw.txt"
with open (caminho_arquivo, 'w') as arquivo:
    arquivo.write('alguma coisa\n')
    arquivo.write('outra coisa \n')
    arquivo.writelines(
        ('linha 3 \n', 'linha 4 \n')
    )
with open (caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())