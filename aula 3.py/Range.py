#RANGE()
#Por ser muito comum a criação de sequências numéricas o python criou uma função onde você passa os critérios para tal sequência e ele a partir disso cria sua sequência.

#Inicio 
#A partir de qual número a sequência será iniciada

#fim
#Em qual número será finalizado, mas o fim da sequência é sempre um número abaixo do qual foi colocado, se por exemplo você colocar para finalizar no número 6 ele irá parar no número 5 a contagem.

#incremento 
#é onde você pode escolher se quer contar de 2 em 2, ou de 3 em 3, ou se quer fazer uma contagem regressiva.

for numero in range(0,10,1):
 print(numero)



#Crie um prorgama onde o usuário vai dizer quantas notas vão ser cadastradas, some as notas e tire a média. no final fale se o aluno foi aprovado ou reprovado.

quantidade = int(input("Digite a quantidade de notas: "))
soma = 0

for numero in range(0, quantidade):
    nota = float(input("Digite a nota: "))
    soma = soma + nota

media = soma / quantidade
print(f"Sua média é {media:.1f}")

if media >= 7:
    print("Aprovado")

elif media >= 5 and media <= 6.9:
 print("recuperação")

else:
 print("Reprovado")