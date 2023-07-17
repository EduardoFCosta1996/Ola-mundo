
x = 5

def escopo():
    
    x=1
    def outro_escopo():
        x = 2
        y = 2
        print(x+y)
    outro_escopo()
    print(x)

escopo()
print(x)