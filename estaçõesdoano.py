def estacao_ano(mes, dia):
    if (mes == 12 and dia >= 22) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        return 'Verão'
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        return 'Outono'
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 23):
        return 'Inverno'
    elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia < 22):
        return 'Primavera'

while True:
    print('\n\n\t\t--Estações do ano--\n\t')

    dia = int(input('Informe o dia: '))
    mes = int(input('Informe o mês: '))

    if 1 <= mes <= 12:
        if mes == 2 and dia > 28:
            print('Dia inválido para o mês informado.')
        elif 1 <= dia <= 31:
            if dia < 0 or mes < 0:
                print('Mês ou dia inválido (números negativos).')
            else:
                estacao = estacao_ano(mes, dia)
                print(f'Estação: {estacao}')
        else:
            print('Dia inválido para o mês informado.')
    else:
        print('Mês inválido')

    resposta = input('Deseja verificar outra data? (s/n): ').lower()
    if resposta != 's':
        break
