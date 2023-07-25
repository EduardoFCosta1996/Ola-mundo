
try:
    a = 18
    b = 0
    a  / b
except ZeroDivisionError:
    print('Error')

except (NameError, IndexError):
    print("Nome error e IndexError")

except Exception:
    print("Error desconhecido")