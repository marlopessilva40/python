def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso!")
        print("Retire o seu dinheiro no caixa eletrônico.")

    print("Obrigado por utilizar o nosso banco!")
    

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Depósito realizado com sucesso! Seu saldo atual é: {saldo}")  


sacar(200)

depositar(300)