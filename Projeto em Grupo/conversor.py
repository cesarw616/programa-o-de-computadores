recomecar= ''
while recomecar!='n' and recomecar!='N':
    
    print('Para Hexadecimal, digite 1 \nPara Octal, digite 2 \nPara Binário, digite 3')
    opcaoConversao=input('Você deseja converter para Hexadecimal, para Octal  ou para Binário?')

    if opcaoConversao=='1':
        num=int(input('Digite o número a ser convertido: '))
        hexa=' '
        dec=num*1
        while num>0:
            resto=num%16
            if resto==10:
                resto='A'
            elif resto==11:
                resto='B'
            elif resto==12:
                resto='C'
            elif resto==13:
                resto='D'
            elif resto==14:
                resto='E'
            elif resto==15:
                resto='F'
            else:
                resto=resto
            hexa=str(resto)+hexa
            num=num//16
        print(f'O decimal {dec} equivale a {hexa} em hexadecimal')

    elif opcaoConversao=='2':
        num=int(input('Digite o número a ser convertido: '))
        octal=' '
        dec=num*1
        while num>0:
            resto=num%8
            octal=str(resto)+octal
            num=num//8
        print(f'O decimal {dec} equivale a {octal} em octal')
    
    elif opcaoConversao=='3':
        num=int(input('Digite o número a ser convertido: '))
        binario=' '
        dec=num*1
        while num>0:
            resto=num%2
            binario=str(resto)+binario
            num=num//2
        print(f'O decimal {dec} equivale a {binario} em binário.')

    else:
        print('erro')

    recomecar=input('Deseja converter outro número?(S/N)')

    if recomecar!='s' and recomecar!='n':
        print('Entrada inválida!')
        recomecar=input('Deseja converter outro número?(s/n')
    else:
        print('Ciência da computação \nElaborado por:\nVictor Giovanni DAnna Nogueira\nGuilherme Oliveira de Souza\nRoberto Messias Dalpino Alves\nMatheus Augusto Gonçalves Mendes \n.\nPojeto interdisciplinar entre:\nPorgramção de computadores\nOrganização e arquitetura de computadores \n.\nmark_1.0')