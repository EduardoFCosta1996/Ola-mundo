import json
CAMINHO_ARQUIVO = 'aula205.json'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Amora', 4)
p2 = Pessoa('Eduardo', 28)
p3 = Pessoa('Nala', 4)
bd =[vars(p1), vars(p2), p3.__dict__]
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('fazendo dump')
        json.dump(bd, arquivo, ensure_ascii=False, indent= 2)
if __name__ == '__main__':
    print('ele é o main')
    fazer_dump( )