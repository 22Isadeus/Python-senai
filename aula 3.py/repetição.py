# Estrutura de repetição 
# Ao desenvolver uma aplicação, é comum deparamos com a necessidade de executar uma mesma instrução por repetidas vezes. Para tanto, as linguagens de programação possuem as chamadas estruturas de repetição, que são estruturas de código que nos permitem executar um bloco de código por uma determinada quantdade de repetições. Em python, temos dois tipos de estruturas de repetição. A primeira delas, o while nos permite repetir a execução de um bloco de código enquanto uma determidnada condição for verdadeira. A segunda estrutura de repetição é o for ... in, que permite executar um bloco de código Para cada elemento de uma sequência.

#estrutura for in
# Em python, a estrutura de repetições for ... in permite executar um bloco de código repetidas vezes, sendo uma repetição para cada elemento em uma sequencia. Em outras palavras, ela permite percorrer (iterar) uma sequência iteravel.
# A estrutura de código for ...in repetirá um determinado bloco de código por um número definido de vezes, que é dado pelo tamanho da sequências que será percorrida.

palavra = str(input('Digite um texto: '))

for letra in palavra:
 Nome = str(input('Digite seu nome: '))
 Idade = int(input(' Digite sua Idade: '))
 Curiosidade = str(input('Digite uma Curiosidade sobre você: '))

 print(f'CADASTRO CONCLUIDO \nNome: {Nome} \nIdade {Idade} \nCuriosidade: {Curiosidade}')
