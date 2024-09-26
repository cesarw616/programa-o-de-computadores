def velocidadeMedia(a,b):
    return (a/b)*3.6

distancia=float(input('Digite a diastancia em metros: '))
tempo=float(input('Digite o tempo em segundos: '))

print(f'{velocidadeMedia(distancia,tempo)}Km/h')