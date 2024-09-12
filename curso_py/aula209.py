class Pessoa:
    ano = 2024  #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def metodo_de_classe(cls):
        print('hey')
    @classmethod
    def criar_50_mais(cls, nome):
        return cls(nome, 50)
    @classmethod
    def anonima(cls, idade):
        return cls('anonima', idade)
p1 = Pessoa('Eduardo', 28)
p2 = Pessoa.criar_50_mais('Amora')
p3 = Pessoa.anonima(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(Pessoa.ano)
Pessoa.metodo_de_classe()

