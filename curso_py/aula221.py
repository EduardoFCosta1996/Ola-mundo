class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        retorno = super().upper()
        return retorno


string = MinhaString('Eduardo')
print(string.upper())