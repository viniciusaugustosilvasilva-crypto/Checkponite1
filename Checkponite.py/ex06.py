valor = float(input("Digite o valor do produto: "))

if valor > 100:
    preco_final = valor * 0.9
    print(f"Preço final com desconto: R${preco_final:.2f}")
else:
    print("Acesso negado.")