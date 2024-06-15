#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['status'] = 'APROVADO'
else:
    aluno['status'] = 'REPROVADO'

print('-' * 40)
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'{aluno["nome"]} está {aluno["status"]}')
