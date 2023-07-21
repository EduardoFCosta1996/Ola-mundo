def saudacao(msg, nome, nome2):
    return f'{msg}, {nome}, {nome2}'
def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, "bom dia", "nome", "eduardo")
print (v)