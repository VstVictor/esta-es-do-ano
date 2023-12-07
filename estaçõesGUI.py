import PySimpleGUI as sg

def estacao_ano(mes, dia):
    if (mes == 12 and dia >= 22) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        return 'Verão'
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        return 'Outono'
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 23):
        return 'Inverno'
    elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia < 22):
        return 'Primavera'


layout = [
    [sg.Text('Informe o dia:'), sg.InputText(key='dia')],
    [sg.Text('Informe o mês:'), sg.InputText(key='mes')],
    [sg.Button('Verificar Estação'), sg.Button('Limpar'), sg.Button('Sair', button_color=('white', 'red'))],  # Adição da vírgula aqui
    [sg.Text('', size=(20, 1), key='resultado')],
]

janela = sg.Window('Estações do Ano', layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Verificar Estação':
        try:
            dia = int(valores['dia'].strip())
            mes = int(valores['mes'].strip())

            if 1 <= mes <= 12:
                if mes == 2 and dia > 28:
                    janela['resultado'].update('Dia inválido para o mês informado.')
                elif 1 <= dia <= 31:
                    if dia < 0 or mes < 0:
                        janela['resultado'].update('Mês ou dia inválido (números negativos).')
                    else:
                        estacao = estacao_ano(mes, dia)
                        janela['resultado'].update(f'Estação: {estacao}')
                else:
                    janela['resultado'].update('Dia inválido para o mês informado.')
            else:
                janela['resultado'].update('Mês inválido')

        except ValueError:
            sg.popup_error('Informe valores numéricos para Dia e Mês.')

    elif evento == 'Limpar':
        janela['dia'].update('')
        janela['mes'].update('')
        janela['resultado'].update('')
        janela['dia'].set_focus()

janela.close()
