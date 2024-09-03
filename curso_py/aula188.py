import os
caminho_arquivo = "C:\\Users\\T-Gamer\\Desktop\\aula\\"
caminho_arquivo += "caminhho.txt"
print(caminho_arquivo)

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Ateção 1 \n')
    arquivo.write('Linha 2\n')
    arquivo.writelines('linha 3\n' 'linha 4\n')
    print(caminho_arquivo)
#os.remove(caminho_arquivo)
#os.rename(caminho_arquivo, 'aula189_a.txt')