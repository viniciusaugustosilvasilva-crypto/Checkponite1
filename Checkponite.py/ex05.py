num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O maior número é {num1}.")
elif num2 > num1:
    print(f"O maior número é {num2}.")
else:
    print("Os números são iguais.")