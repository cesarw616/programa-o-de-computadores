def exibirMensagem(nome):
    print(f'Olá {nome}!')
    print('Estou no método...')
    ateLogo()

def ateLogo():
    print('Até logo!')

nome= input('Qual o seu nome?')
exibirMensagem(nome)