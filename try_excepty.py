
try:
    a = 18
    b = 0
    a  / b
except ZeroDivisionError:
    print('Error')

except (NameError, IndexError):
    print("Nome error")

except Exception:
    print("Error desconhecido")