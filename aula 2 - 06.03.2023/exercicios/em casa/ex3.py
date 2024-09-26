#Escreva um programa em Python que solicite ao usuário a
#distância entre duas cidades e o tempo de viagem. O
#programa deverá calcular e exibir a velocidade média de um
#carro que vai de uma cidade para outra

distancia=float(input('Digite a distancia entre a cidade A e a cidade B em Km: '))
tempo=float(input('Digite o tempo de viagem entre as duas cidades em horas: '))
Vm=(distancia/tempo)
print('A velocidade média durante a viagem foi de %s Km/h'%Vm)