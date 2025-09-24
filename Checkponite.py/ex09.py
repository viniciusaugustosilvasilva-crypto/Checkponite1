temperatura = float(input("Digite a temperatura em graus Celsius: "))

if temperatura < 0:
    print("Conlante")
elif 0 <= temperatura <= 30:
    print("Agradável")
else:
    print("Quente")