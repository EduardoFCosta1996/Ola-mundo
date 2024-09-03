import json

with open('aula190_a.json', 'r',encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
