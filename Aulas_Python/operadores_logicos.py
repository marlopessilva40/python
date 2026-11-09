saldo = 1000
saque = 200
limite = 100
conta_especial = True

print(True and True)
print(True and False)
print(False and False)
print(True or True) 
print(True or False)


print (saldo >= saque)

print (saque <= limite)

retirar = saldo >= saque and saque <= limite
print (retirar)

retirar = (saldo >= saque and saque <= limite) or (conta_especial and saque <= limite)

