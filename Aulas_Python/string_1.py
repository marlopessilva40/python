nome = 'MarcElo LoPes da SiLVA'


print(nome.upper())
print(nome.lower())
print(nome.title())



#### eliminar espaços

texto = "  Olá, tudo bem?   "
print(texto + ".")
print(texto.strip()+ ".")

print(texto.lstrip() + ".") #direita
print(texto.rstrip()+ ".") #esquerda

###junçao e centralizaçao

menu = "Python"
print("####"+menu+"####")
print(menu.center)
print(menu.center(20, "#"))


##join
print ("P-y-t-h-o-n") 
print ("-".join(menu))