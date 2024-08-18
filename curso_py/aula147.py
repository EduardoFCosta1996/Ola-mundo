def generator(n=0, maximo = 10):
    while True:
        yield n
        if n >= maximo:
            return
        n +=1

gen = generator(n=5, maximo=9)

for n in gen:
    print(n)