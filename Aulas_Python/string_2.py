nome = "Marcelo Lopes da Silva"
idade = 60
profissao = "Professor"
linguagem = "Python"   


print("Nome: %s Idade: %d" % (nome, idade   ))   


print("Nome: {} Idade: {}".format(nome, idade))

#posiçao  reaproveitamento  {}
print("Nome: {1} Idade: {0}".format(idade, nome))

#nomeado
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))


#utilizando lista
dados = {"nome": "Marcelo", "idade": 60, "profissao": "Professor"}
print("Nome: {nome} Idade: {idade}".format(**dados))


#f-strings
print(f"Nome: {nome} Idade: {idade} Profissao: {profissao} Linguagem: {linguagem}")

saldo = 1000.50
print(f"Nome: {nome} Idade: {idade}  Saldo: {saldo:.2f}")  #formataçao de casas decimais