placas=[]
multas=[]
maiores=[]
soma=0

for i in range(15):
    placa=input('Digite a placa do veiculo: ')
    placas.append(placa)
    multa=float(input(f'Digite o valor da multa para o veiculo de placa {placa}: '))
    multas.append(multa)
    if multa>=300: maiores.append(placa)
    soma= soma+multa

media=soma/15
print(placas,multas,maiores,media)
