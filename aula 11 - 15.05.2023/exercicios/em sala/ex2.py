nomes=[]
for i in range(5):
    nome=input(f'Digite {i+1}° nomes: ')
    nomes.append(nome)
n=int(input('Digite um número: '))
if n>len(nomes):
    print('Nome não encontrado')
else:
    print(nomes[n])