#texto = input("Digite um texto: ")
texto = " "
VOGAIS = "AEIOU"    

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()
    print("Fim do programa, todas as letras foram verificadas!")