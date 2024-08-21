def concatenar(str_incial):
        valor_final = str_incial
        def interna(valor_concatenar):
            nonlocal valor_final
            valor_final+=valor_concatenar
            return valor_final
        return interna

c = concatenar('a')
print(c('v'))
print(c('e'))
print(c('r'))
final = c()
print(final)