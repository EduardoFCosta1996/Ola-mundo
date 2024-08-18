

try:
    a = 18
    #b = 0
    c = a/b
    print('linha1')
except ZeroDivisionError:
    print('erro')
except NameError:
    print('continuou sem erro')
    