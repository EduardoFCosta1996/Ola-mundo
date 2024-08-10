
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
a = int(input ("digite um numero: "))
a % 2 == 0
if a % 2 == 0:
    print("numero par")

else:
    print("numero impar")
"""






"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
a= int(input("digite a hora"))

if a >= 0 and a <= 11:
    print("dia")
elif a >= 7 and a <= 12:
    print("tarde")
else:
    print('noite')
"""



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = len(input("digite seu nome"))

if nome <=4:
    print("nome curto")
elif nome <= 6:
    print("medio")
else:
    print('grande')