#del
#Para excluir uma informação da lista utilizamos o del

alunos = ['Amanda', 'Rodrigo', 'Davi', 'Paula']
print(alunos)
excluir = int(input('escreva a posição do aluno que dese=ja excluir: '))

del alunos[excluir]
print(alunos)