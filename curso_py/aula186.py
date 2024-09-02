caminho_arquivo = "C:\\Users\\T-Gamer\\Desktop\\aula\\"
caminho_arquivo += "caminhho.txt"
print(caminho_arquivo)
#with open(caminho_arquivo,'w') as arquivo:
#    print('Óla mundo')
#    print('arquivo vai ser fechado')


with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2\n')
    arquivo.writelines('linha 3\n' 'linha 4\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())