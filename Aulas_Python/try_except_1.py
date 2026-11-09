try:
    numero = 10/0
except ZeroDivisionError:
    print("Não é possível dividir por zero")

try:
    numero = int("afv")
    print (numero)
except ValueError:
    print("Não é possível converter para inteiro")
finally:
    print("Fim do programa")