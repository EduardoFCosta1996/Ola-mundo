def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        resultado += 'alguma coisa'
        print('ok você foi decorado')
        return resultado
    return interna
@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


#inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('123')
print(invertida)