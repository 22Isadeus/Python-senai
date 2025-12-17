#Operadores Lógicos

#Os operadores lógicos, como o próprio nome diz, são operadores que permitem realizar operações lógicas entre valores booleanos e o resultado será sempre verdadeiro (True) ou falso (False). Estes operadores são importantes para a formação de lógicas completas, em conjunto com outros operadores, que possibilitam a verificação de diferentes condições no programa. Fazem parte desta categoria os seguintes operadores lógicos:

#Símbolo | Descrição | Utilização

#and
#Retorna verdadeiro (True) se, e somente se, os dois valores colocados sejam verdadeiros.
#Utilização: x and y

#or
#Retorna verdadeiro (True) se qualquer um dos dois seja verdadeiro e retorna falso (False) se, e somente se, os dois forem falsos.
#Utilização: x or y

#not
#Retorna verdadeiro (True) se o valor for falso (False), retorna falso (False) se o valor for verdadeiro (True).
#Utilização: x not y

Nome = str(input('digite seu nome: '))
idade=int(input('digite sua idade: '))
tempo_contribuição = int(input('digite seu tempo de contribuição em anos: '))

if(idade >= 65 and tempo_contribuição >=30) or Nome == 'Carlos':
    print('pode se aposentar')