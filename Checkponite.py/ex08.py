numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("Par")
elif numero % 5 == 0:
    print("Múltiplo de 5")
else:
    print("Outro número")