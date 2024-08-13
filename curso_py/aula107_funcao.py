"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1
def funcao():
    def outra_funcao():    
        y=2
        print(x,y,)
        def mais_uma():
            h = 3
            print(h,x,y)
        mais_uma()
            
    outra_funcao()
    print(x)
funcao()