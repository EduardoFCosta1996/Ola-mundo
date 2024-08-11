for i in range(10):

    if i == 2:
        print("i igual a 2 pulou")
        continue
    if i == 8:
        print("i 8 não sera executado")
        break
    for j in range(1, 3):
        print(i ,j)
else:
    print("for completo")