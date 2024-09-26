#Escreva um programa em Python que obtenha uma temperatura em graus Celsius,
#calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin. 

celsius=int(input('Digite a temperatura em graus Cesius: '))
fr=(1.8*celsius)+32
tk=celsius+273

txt="As temeperaturas em graus Kelvim e em Fareheit são, respectivamente:{0} e {1}"
print(txt.format(tk,fr))