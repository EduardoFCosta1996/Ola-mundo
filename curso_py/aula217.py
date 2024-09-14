class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    def __del__(self):
        print('apagando,', self.nome)
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    def __del__(self):
        print('apagando,', self.rua, self.numero)

cliente1 = Cliente('maria')
cliente1.inserir_endereco('rua visconde', 40)
cliente1.inserir_endereco('castelli', 170)
print(cliente1.enderecos[0].rua)
cliente1.listar_endereco()