#consulta
#conseguimos consultar se um aluno pertence ao grupo ou não

alunos = ['Pedro', 'João', 'Romario', 'Adalberto']

consulta = str(input('Digite um nome a ser consultado: '))

if consulta in alunos:
    print('O nome está na turma')

else:
    print('O nome não está na tuma')