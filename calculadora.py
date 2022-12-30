#tela inicial
print('Olá, escolha uma das opções abaixo.')

print()

print('0 : Soma')
print('1 : Subtração')
print('2 : Multiplicação')
print('3 : Divisão')
print('4 : Exponenciação')

print()

operacao = int(input('Operação escolhida: '))
print()

#Soma
if operacao == 0:
    print('*** A operação escolhida foi Soma (+) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 + n2
    print()
    print('O valor da soma é {:.1f}'.format(n))

#Subtração
if operacao == 1:
    print('*** A operação escolhida foi Subtração (-) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 - n2
    print()
    print('O valor da subtração é {:.1f}'.format(n))

#Multiplicação
if operacao == 2:
    print('*** A operação escolhida foi Multiplicação (*) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 * n2
    print()
    print('O valor da multiplicação é {:.1f}'.format(n))

#Divisão
if operacao == 3:
    print('*** A operação escolhida foi Divisão (*) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 / n2
    print()
    print('O valor da divisão é {:.1f}'.format(n))

#Exponenciação
if operacao == 4:
    print('*** A operação escolhida foi Exponenciação (**) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 ** n2
    print()
    print('O valor da exponenciação é {:.1f}'.format(n))      