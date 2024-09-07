class animal:
    def __init__(self, nome):
        self.nome = nome
        variavel = 'valor'
        print(variavel)
    
    def acao(self):
       return f'{self.nome} esta excutando a acao, pq self pega dados da classe,self faz ter acesso a todos os metodos'

leao = animal(nome='leao')
print(leao.nome)
print(leao.acao())