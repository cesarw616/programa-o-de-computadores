dias=[]
volumes=[]
soma=0
for i in range(10):
    dia=input('Digite o dia da semana: ')
    dias.append(dia)
    volume=input(f'Digite o vaolume de chuva do dia {dia}: ')
    volumes.append(volume)

opcao=input('Digite o dia que deseja ver a media: ')
divisor=dias.count(opcao)
while True:
    i= dias.index(opcao)
    dias.pop(i)
    soma=soma+float(volumes[i])
    volumes.pop(i)
    if opcao not in dias: break

media=soma/divisor
print(media)