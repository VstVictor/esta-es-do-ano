def estacao_ano(mes, dia):
    if (mes == 12 and dia >= 22) or (mes == 1 or mes == 2) or (mes == 1 or mes == 3 and dia < 21):
        return 'Verão'
    elif (mes == 3 and dia >= 21) or (mes == 4 and mes == 5) or (mes == 6 and dia < 21):
        return 'Outono'
    elif (mes == 6 and dia >= 21) or (mes == 7 and mes == 8) or (mes == 9 and dia < 23):
        return 'Inverno'
    elif (mes == 9 and dia >=23) or (mes == 10 or mes == 11) or (mes == 12 and dia <22):
        return 'Primavera'

# Apresentação
print('\n\n\t\t--Estações do ano--\n\t')

# Entrada
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))

# Verificações
if 1 <= mes <= 12:
    if mes == 2 and dia > 28:
        print('Dia inválido para o mês de informado.')
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
