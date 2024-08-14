def criar_saudacao(saudacao):
    def saudar(nome):
        return(f'{saudacao}, {nome}')
    return saudar

bd = criar_saudacao("bom dia")
bn = criar_saudacao("boa noite")

for nome in ["eduardo", "costa"]:
    print(bd(nome))
    print(bn(nome))