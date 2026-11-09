saldo = 2000
saque = 5000

idade = 18

status = "Saque realizado com sucesso!" if saldo >= saque else "Saldo insuficiente para saque!" 
print(f'{status} ao realizar o saque')


condicao = "Voce é maior de idade!" if idade >= 18 else "Você é menor de idade!"
print(f'{condicao} ao verificar a idade')