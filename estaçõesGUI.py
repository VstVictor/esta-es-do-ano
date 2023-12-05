import PySimpleGUI as psg
import estaçõesdoano  # Assuming you have a module named 'estaçõesdoano' with a 'cel' function

layout = [
    [psg.Text('Informe o dia: '), psg.InputText(key='input_dia')],
    [psg.Text('Informe o mês: '), psg.InputText(key='input_mes')],
    [psg.Text('Dia:'), psg.Text('', key='output_dia')],
    [psg.Text('Mês:'), psg.Text('', key='output_mes')],
    [psg.Button('Estação')]
]

janela = psg.Window('Estações do ano', layout)

while True:
    evento, estacao = janela.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Estação':
        try:
            dia = int(estacao['input_dia'])
            mes = int(estacao['input_mes'])
            janela['output_dia'].update(estaçõesdoano.dia(dia, mes))
            janela['output_mes'].update(estaçõesdoano.mes(dia, mes))

        except ValueError:
            pass

janela.close()



