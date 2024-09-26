import os, math
os.system('cls')

a=float(input('Digite, em m², o tamanho da área a ser pintada: '))
l=a/3
latas=(math.ceil(l/18))

print(f'Para pintar uma partede de {a} m², você precisará de {latas} litro(s) de tinta \nO valor total será de R${latas*80:.2f}')