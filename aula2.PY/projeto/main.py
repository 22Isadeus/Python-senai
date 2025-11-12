nome_cliente = input("insira o nome:"). title()
idade_cliente = input("informe sua idade:")
idade_cliente = int(idade_cliente)
nome_do_fime = "Gente Grande"
valor_ingresso = 75.00
Meio_ingresso = valor_ingresso/2


print(f"Seja bem-vindo (a) {nome_cliente}")
print(f"O filme que está em cartaz é {nome_do_fime}")
print(f"ingresso inteiro é R$ {valor_ingresso} e o meio é {Meio_ingresso:.2f}")

quatidade_de_ingressos = input('quantos ingressos voçê quer comprar:')
quantidade_de_ingressos = int(quatidade_de_ingressos)

if idade_cliente <= 24 or idade_cliente >= 60:
    valor_final = quantidade_de_ingressos*Meio_ingresso
#if significa verdadeiro então se a idade for menor ou iguar a 24 sera meio valor e o else completa. Pois será o resto no caso 25 a maior.
else : 
    valor_final = quantidade_de_ingressos * valor_ingresso

if quantidade_de_ingressos <= 3:
    valor_final *= 0.95

elif quantidade_de_ingressos <= 5:
    valor_final *= 0.90

elif quantidade_de_ingressos <= 10:
    valor_final *= 0.80

else :
    valor_final *= 0.70

print(f'Sua compra saiu o total de R${valor_final:.2f}')
