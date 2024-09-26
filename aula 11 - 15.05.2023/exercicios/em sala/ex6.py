nomes=[]
for i in range(5):
    nome=input(f'digite o nome do {i+1} usuario: ')
    nomes.append(nome)

print(30*'-')
print(nomes)
print(f'a lista possui {len(nomes)} nomes')
print(30*'-')

nome=input('digite um nome para remover: ')
while len(nomes)>0:
    if nome in nomes:
        nomes.remove(nome)
    else:
        print(f'{nome} nao esta na lista')
    print(nomes)
    print(f'a lista possui {len(nomes)} nomes')