class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        retorno = super(MinhaString, self).upper()
        return retorno


string = MinhaString('Eduardo')
print(string.upper())