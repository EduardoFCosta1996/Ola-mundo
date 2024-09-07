class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        

p1 = Pessoa('Eduardo', 'Costa')
#p1.nome = 'Eduardo'
#p1.sobrenome= 'Costa'

p2 = Pessoa('Amora', 'Nala')
print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)