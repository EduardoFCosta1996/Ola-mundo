class Camera:
    def __init__(self,nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando')
            return
        print(f'{self.nome} esta filmando')
        self.filmando = True
    def fotografando(self):
        if self.filmando:
            print('a camera está filmando')
            return
        print(f'{self.nome} está fotografando')


c1 = Camera('Camera x')
c2 = Camera('Camera y')
c1.fotografando()
c1.filmar()
c1.filmar()
c2.filmar()
#print(c2.filmando)       