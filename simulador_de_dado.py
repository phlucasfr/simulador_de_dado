import random
import PySimpleGUI as Sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [Sg.Text('Jogar o dado?')],
            [Sg.Button('Sim'), Sg.Button('Não')]
        ]

    def iniciar(self):
        self.janela = Sg.Window('Simulador de Dado', layout=self.layout)
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao recerber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()
