conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2005
cheque_especial = 450

if conta_normal:    
    if saldo >= saque:
        print('saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com uso do cheque especial!')
    else:
        print('Não foi possível realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    else:
        print('saldo insuficiente para saque!')
else:
    print('Tipo de conta inválida!')    