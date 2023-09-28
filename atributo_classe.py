#ano_atual = 2023
class pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ano_atual = 2023
        return ano_atual - self.idade
    
p1 = pessoa("Eduardo", 27)
p2 = pessoa("s", 21)
print(p1.nome, p1.get_ano_nascimento())
print(p2.nome, p2.get_ano_nascimento())