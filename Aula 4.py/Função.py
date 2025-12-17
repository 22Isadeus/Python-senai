#funções
#para definir uma nova função, utilizaremos a instrução def.
#def nome_da_funcao(argumento1, argumento2,....)
#<bloco de código a ser executado>
#return resultado

#Diferentemente do que já vimos até agora, essas linhas não serão executadas imediatamente, exceto a definição da função em si. Na realidade, a definição prepara o interpretador para executar a função quando esta for chamada em outras partes do programa

def soma(a,b):
    print(a + b)

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

soma(numero1, numero2)

numero1 = float(input('digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

soma(numero1, numero2)