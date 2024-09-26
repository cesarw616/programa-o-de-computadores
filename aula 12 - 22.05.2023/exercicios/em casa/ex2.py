def parcela(a,b):
    return (a/b)+((a/b)*(5/100))

valorComrpa=float(input('Digite o valor total da compra: '))
quantidadeParcelas=int(input('Digite a quantidade de parcelas: '))

print(parcela(valorComrpa,quantidadeParcelas))