#com pop excluirmos da lista, mas ele ainda continua armazenando
alunos = ['Amanda', 'Rodrigo', ' Davi', 'Paula']

print(alunos)

excluir = int(input('escreva a posição do aluno que deseja excluir: '))

excluido = alunos.pop(excluir)

print(excluido)
print(alunos)