km_rodados = int(input("Quantos km você rodou? "))

# Cálculo do valor da corrida usando if e elif
if km_rodados <= 150:
    valor_corrida = km_rodados * 50  # 0,50 por km = 50 centavos
    print(f"Você rodou {km_rodados} km. Valor da corrida: R$ {valor_corrida/100:.2f}")
elif km_rodados > 150:
    valor_corrida = 150 * 50 + (km_rodados - 150) * 80  # 0,50 até 150 km e 0,80 após
    print(f"Você rodou {km_rodados} km. Valor da corrida: R$ {valor_corrida/100:.2f}")
else:
    print("Valor inválido.")  # Caso a entrada seja negativa
    