# SCRIPT PARA VERIFICAR SE É VIÁVEL O INVESTIMENTO EM UMA AÇÃO
import numpy as np

print('-'*50)
print('VALIDAÇÃO DE INVESTIMENTO EM UMA AÇÃO')
print('-'*50)

def teste1():
    pl = float(input('\nDigite o valor de P/L da empresa: ')) # Preço/Lucro
    pvp = float(input('Digite o valor de P/VP da empresa: ')) # Preco/Valor Patrimonial
    if pl < 16 and pvp < 1.7:
        valida1 = True
        print('\nOk, a princípio a ação está compensando, vamos prosseguir...')
        conf = 'a'
    else:
        valida1 = False
        conf = input('\nA ação não está compensando, deseja testar com outra empresa? (s/n): ')
    return valida1,conf

def teste2():
    preco_acao = float(input('\nDigite o preço da ação: ')) # Preço da ação
    lpa = float(input('Digite o valor de LPA da empresa: ')) # Lucro por ação
    vpa = float(input('Digite o valor de VPA da empresa: ')) # Valor patrimonial por ação
    vi = np.round(np.sqrt(22.5*lpa*vpa),2)
    if preco_acao <= vi:
        valida = True
        print('\nA ação está compensando ser comprada!')
        print('O preço justo é de R$ ',vi, ' reais')
        conf = input('\nDeseja testar com outra empresa? (s/n): ')
    else:
        valida = False
        print('\nA ação NÃO está compensando ser comprada')
        print('O preço justo é de R$ ',vi, ' reais')
        conf = input('\nDeseja testar com outra empresa? (s/n): ')
    return valida,conf

valida1 = True
while valida1 == True:
    valida1,conf = teste1()
    if valida1:
        valida2,conf = teste2()
        if not valida2:
            if conf == 's':
                valida1 = True
            elif conf == 'n':
                print('\nObrigado, até a próxima!')
                break
        else:
            if conf == 's':
                valida1 = True
            elif conf == 'n':
                print('-'*50)
                print('\nObrigado por utilizar o programa, volte sempre! :)')
                break
    elif conf == 's':
        valida1 = True
    elif conf == 'n':
        print('\nObrigado, até a próxima!')
        break
