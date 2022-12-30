def soma():
    print('*** A operação escolhida foi Soma (+) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 + n2
    print()
    print('O valor da soma é {:.1f}'.format(n))

def subtracao():
    print('*** A operação escolhida foi Subtração (-) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 - n2
    print()
    print('O valor da subtração é {:.1f}'.format(n))

def multiplicacao():
    print('*** A operação escolhida foi Multiplicação (*) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 * n2
    print()
    print('O valor da multiplicação é {:.1f}'.format(n))

def divisao():
    print('*** A operação escolhida foi Divisão (*) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 / n2
    print()
    print('O valor da divisão é {:.1f}'.format(n))

def exponenciacao():
    print('*** A operação escolhida foi Exponenciação (**) ***')
    print()
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    n = n1 ** n2
    print()
    print('O valor da exponenciação é {:.1f}'.format(n))   

while True:
    print('Olá, escolha uma das opções abaixo.')
    
    print()
    
    print('0 : Soma')
    print('1 : Subtração')
    print('2 : Multiplicação')
    print('3 : Divisão')
    print('4 : Exponenciação')
    
    print()
    
    menu = int(input('Operação escolhida: '))
    
    print()
    
    if menu == 0:
        soma()
    elif menu == 1:
        subtracao()
    elif menu == 2:
        multiplicacao()
    elif menu == 3:
        divisao()
    elif menu == 4:
        exponenciacao()
    else:
        print('Valor inválido')

    while True:
        opcao = input('Deseja realizar outra operação? (S/N)? ').upper()
        if opcao not in ('S', 'N'):
            print('Opção inválida, deve ser S ou N')
        else:
            break
        if opcao == 'N':
            break        