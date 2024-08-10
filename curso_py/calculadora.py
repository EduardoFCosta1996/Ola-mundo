


while True:
    numero1 = input("digite um numero")
    numero2 = input("digite outro numero")
    operador = input("digite o operdador (+-*/)")
    numero_valido = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numero_valido = True
    except:
        numero_valido = None
    if numero_valido is None:
        print("um dos dois numeros sao invalidos")
        continue
    operadores_permitidos = "+-*/"
    if operador not in operadores_permitidos:
        print("operador nao permitido")
        continue
    if len(operador) > 1:
        print("digite apenas 1 operador")
        continue

    if operador == "+":
        print(num_1_float + num_2_float)

    elif operador == "-":
        print(num_1_float - num_2_float)
    elif operador == "*":
        print(num_1_float * num_2_float)
    elif operador == "/":
        print(num_1_float / num_2_float)
    else:
        print("Não era para chegar aqui")



    sair =input(print("Sair digite [s]")).lower().startswith("s")
    if sair is True:
        break
