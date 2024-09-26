import os
os.system('cls' or 'clear')
#Exemplo 1- aula 2; testando maneiras de usar a função print
nome=input('Digite se nome: ')
disciplina=input('Digite a matéria: ')
nota1=float(input('Digite a nota A1: '))
nota2=float(input('Digite a nota A2: '))
media=(nota1+nota2)/2
print(f'O aluno {nome} obteve as notas {nota1} e {nota2} em {disciplina},\n portanto sua media será {media}')
print('Aperte enter para continuar...')
