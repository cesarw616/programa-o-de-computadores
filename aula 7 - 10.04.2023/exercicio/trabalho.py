import os

os.system('cls' or 'clear')

def decimal_para_base(number, base):
    if base == 2:
        return bin(number)[2:]
    elif base == 8:
        return oct(number)[2:]
    elif base == 16:
        return hex(number)[2:].upper()

def base_para_decimal(number, base):
    if base == 2:
        return int(str(number), 2)
    elif base == 8:
        return int(str(number), 8)
    elif base == 16:
        return int(str(number), 16)

print("Selecione a operação que deseja realizar:")
print("1. Conversão de decimal para binário, octal e hexadecimal")
print("2. Conversão de binário, octal e hexadecimal para decimal")

opcao = int(input("Digite a opção desejada (1 ou 2): "))

if opcao == 1:
    decimal = int(input("Digite o número decimal que deseja converter: "))
    print("O número", decimal, "em binário é:", decimal_para_base(decimal, 2))
    print("O número", decimal, "em octal é:", decimal_para_base(decimal, 8))
    print("O número", decimal, "em hexadecimal é:", decimal_para_base(decimal, 16))
elif opcao == 2:
    base = int(input("Digite a base do número que deseja converter (2, 8 ou 16): "))
    number = input("Digite o número que deseja converter: ")
    print("O número", number, "em decimal é:", base_para_decimal(number, base))
else:
    print("Opção inválida. Tente novamente.")