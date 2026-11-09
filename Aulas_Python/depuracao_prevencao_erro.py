try:
    numero = int(input("Ingrese un número: "))
    print(10/numero)
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except ValueError:
    print("Digite apenas números inteiros")  