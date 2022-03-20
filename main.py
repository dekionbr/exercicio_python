import os
from pa import Pa
from apuracao import Apuracao

def clear():
    os.system('cls||clear')

def menu_pa(valor_razao, valor_termo1):
    print('*** Progressão Aritmética ***')
    pa = Pa(valor_termo1,valor_razao)
    pa.calcular()
    input('aperte qualquer tecla para continuar')

def menu_apuracao():
    apuracao = Apuracao([])
    menu = '0'
    while (menu != '-1'):
        clear()
        print('*** Apuração de Votos ***')
        print('1 - para votar')
        print('2 - para apurar os votos')
        print('Digite -1 para sair do programa')
        menu = input('Digite o que deseja fazer: ')

        if(menu == '1'):
            clear()
            print('Confira os candidatos a seguir:')
            print('1 - João da Silva')
            print('2 - José Ramalho')
            print('3 - Maria Mattos')
            print('4 - Pedro Américo')
            voto = input('Digite o numero do candidato desejado: ')
            apuracao.set_voto(voto)

        if(menu == '2'):
            apuracao.apurar()

        input('digite qualquer tecla para continuar')


def menu_primo():
    print('*** Numero Primo ***')
    numero=int(input('digite um numero para saber se ele é primo: '))
    mult=0
    for count in range(1,numero+1):
        if(numero % count == 0):
            mult += 1
    if(mult==2):
        print('É primo')
    else:
        print(f'Não é primo')

    input('aperte qualquer tecla para continuar')

def menu_financeiro():
    print('*** Calculo do financiamento ***')
    r = int(input('Entre com a taxa de juros de financiamento price: ')) / 100
    pmt = float(input('Entre com o valor das parcelas: '))
    n = int(input('Entre com o numero de parcelas financiadas: '))
    calc = n*(pmt / (1+r)**1)
    print(f'Valor final do financiamento: {calc:.2f}')
    input('aperte qualquer tecla para continuar')

while True:
    clear()
    print("*** Menu de exercícios ***")
    print('1 - progressão aritmética')
    print('2 - apuração de votos')
    print('3 - Numero primo')
    print('4 - Calculo do financiamento')
    print('Para fechar digite -1')
    menu = input('Escolha o programa: ')

    if(menu == '1'):
        clear()
        valor_termo1 = input('Entre com o primeiro termo: ')
        valor_razao = input('entre com a razão: ')
        menu_pa(valor_razao, valor_termo1)

    if(menu == '2'):
        clear()
        menu_apuracao()

    if(menu == '3'):
        clear()
        menu_primo()

    if(menu == '4'):
        clear()
        menu_financeiro()

    if(menu == '-1'):
        break
