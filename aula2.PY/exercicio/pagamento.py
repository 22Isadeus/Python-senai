# Entrada do valor da compra
valor_compra = input("Digite o valor da compra: R$ ")
valor_compra = int (valor_compra)

# Exibe as opções de pagamento
print("""
Escolha a forma de pagamento:
1 - À vista Dinheiro (10% de desconto)
2 - À vista Cartão (2% de desconto)
3 - À vista PIX (25% de desconto)
4 - 2x no Cartão (0% de desconto)
5 - 3x ou mais no Cartão (20% de juros)
""")

# Entrada da opção escolhida
opcao = int(input("Digite o número da opção desejada: "))

# Calcula o valor final conforme a opção escolhida
if opcao == 1:
    desconto = 0.10
    valor_final = valor_compra * (1 - desconto)
    print("Você recebeu 10% de desconto.")
elif opcao == 2:
    desconto = 0.02
    valor_final = valor_compra * (1 - desconto)
    print("Você recebeu 2% de desconto.")
elif opcao == 3:
    desconto = 0.25
    valor_final = valor_compra * (1 - desconto)
    print("Você recebeu 25% de desconto.")
elif opcao == 4:
    desconto = 0.0
    valor_final = valor_compra
    print("Sem desconto.")
elif opcao == 5:
    juros = 0.20
    valor_final = valor_compra * (1 + juros)
    print("Foi aplicado 20% de juros.")
else:
    valor_final = valor_compra
    print("Opção inválida. Valor sem alteração.")

# Mostra o valor final
print(f"Valor final a pagar: R$ {valor_final:.2f}")
